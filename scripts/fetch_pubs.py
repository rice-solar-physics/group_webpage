"""
Fetch and parse publications from ADS and print to YAML to be displayed
on group webpage. Uses the Python bindings for the APS API
"""

import logging
import argparse
import os
import sys
import datetime

import ads
import yaml


class FetchPubs(object):
    """
    Class for querying ADS for publication information, compiling to YAML
    """

    def __init__(self, pub_db, ads_key=os.path.join(os.environ['HOME'],'.ads/dev_key'),  
                 people=[], people_db='', max_pub_count_debug=1e+10, year_cutoff=2010):
        self.journal_name_keywords = ['astronomy', 'astrophysics', 'astrophysical', 'astronomical', 'solar', 'royal society','plasmas']
        self._config_logger()
        self._set_key(ads_key)
        self.pub_db = pub_db
        self.max_pub_count_debug = max_pub_count_debug
        self.year_cutoff = year_cutoff
        if people:
            self.people = people
        else:
            self.people = self.read_people(people_db)

    def _set_key(self, ads_key):
        """Set token to query ADS"""
        if os.path.exists(ads_key):
            self.logger.debug('Setting ADS key from file %s'%ads_key)
            with open(ads_key,'r') as f:
                self.my_ads_key = f.read()
            f.close()
        else:
            self.my_ads_key = ads_key
        ads.config.token = self.my_ads_key

    def _config_logger(self):
        """Configure logger instance"""
        self.logger = logging.getLogger(type(self).__name__)
        #self.logger.setLevel(logging.DEBUG)
        #ch = logging.StreamHandler(sys.stdout)
        #ch.setLevel(logging.DEBUG)
        #self.logger.addHandler(ch)

    def read_people(self,people_db):
        """Parse YAML config file containing author information"""
        with open(people_db,'r') as f:
            people = yaml.load(f)
        people_list = []
        for p in people:
            if p['role'] != 'alum':
                try:
                    people_list += p['pub_name']
                    self.logger.info("Adding authors: {}".format(','.join(p['pub_name'])))
                except KeyError:
                    self.logger.exception("No pub names found for {}".format(
                                            ' '.join([p['first_name'],p['last_name']])))

        return people_list

    def query_db(self):
        """Query ADS for publications by all self.people"""
        self.top_level_pubs = dict()
        request_count = 0
        for a in self.people:
            self.logger.info("Querying author: %s"%a)
            tmp = list(ads.SearchQuery(author=a))
            request_count += 1
            self.logger.debug("Request # %d"%request_count)
            self.top_level_pubs[a] = []
            pub_count = 0
            for t in tmp:
                if not self.filter_pubs(t):
                    self.logger.debug("Skipping %s, (%s)"%(t.title,t.year))
                    continue
                #Flag Rice authors
                tmp_rsp_auth = []
                for ta in t.author:
                    if ta in self.people:
                        tmp_rsp_auth.append(ta)
                try:
                    citation_count = len(t.citation)
                except TypeError:
                    citation_count = 0
                self.top_level_pubs[a].append({'title':t.title,
                   'author':t.author,
                   'rs_author':tmp_rsp_auth,
                   'year':t.year, 'pub':t.pub,
                   'bibcode':t.bibcode,
                   'property':t.property,
                   'volume':t.volume,
                   'page':t.page,
                   'citation_count':citation_count,
                   'date':'-'.join(['01' if dt=='00' else dt for dt in t.pubdate.split('-')])})
                self.logger.debug("Storing paper: %s"%t.title)
                #pub counts for debugging
                pub_count += 1
                if pub_count >= self.max_pub_count_debug:
                    self.logger.debug("Breaking at pub count %d for debugging."%self.max_pub_count_debug)
                    break

    def flatten_and_sort(self):
        """Flatten publication list and sort by year"""
        flat_pubs = [pub for authors in self.top_level_pubs for pub in self.top_level_pubs[authors]]
        #Remove duplicates
        #TODO: a more compact way to do this; currently not very pythonic
        _tmp = []
        _tmp_titles = []
        for pub in flat_pubs:
            if pub['title'] not in _tmp_titles:
                _tmp_titles.append(pub['title'])
                _tmp.append(pub)
        flat_pubs = _tmp
        self.flat_pubs = sorted(flat_pubs,
            key=lambda k: datetime.datetime.strptime(k['date'],'%Y-%m-%d'),
            reverse=True)

    def filter_pubs(self,paper):
        """Filter publication list"""
        check_flag = False
        for key in self.journal_name_keywords:
            try:
                if key in paper.pub.lower():
                    check_flag = True
                    break
            except TypeError:
                pass
        if int(paper.year) < self.year_cutoff:
            check_flag = False
        if 'NOT REFEREED' in paper.property:
            check_flag = False

        return check_flag

    def pubs2yaml(self):
        """Print publication list to YAML config file"""
        if not self.flat_pubs:
            self.logger.warning("Printing empty publiction list to %s. Set publication list with self.flatten_and_sort()"%self.pub_db)
        pub_container = {'pubs':self.flat_pubs}
        pub_container['years'] = sorted(list(set(
                        [pub['year'] for pub in self.flat_pubs])),reverse=True)
        self.logger.info("Printing publication list to %s"%self.pub_db)
        with open(self.pub_db,'w') as yf:
            yf.write(yaml.dump(pub_container,default_flow_style=False))


if __name__=='__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Query ADS database for publications from the Rice Solar Physics Research Group')
    parser.add_argument("-k","--ads_key",help="Path to file containing ADS key needed to query database")
    parser.add_argument("-d","--pub_db",help="YAML file to write publication entries to")
    parser.add_argument("--people_db",help="YAML file containing author info")
    args = parser.parse_args()
    # Publication fetcher class
    pub_finder = FetchPubs(args.pub_db, people=['Bradshaw, S. J.', 'Bradshaw, Stephen', 'Barnes, W. T.'], 
                           people_db=args.people_db, ads_key=args.ads_key)
    pub_finder.query_db()
    pub_finder.flatten_and_sort()
    pub_finder.pubs2yaml()
