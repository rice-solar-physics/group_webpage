#name: fetch_pubs.py
#author: Will Barnes
#date: 17 January 2015
#description: class for fetching and parsing publications from ADS

import yaml
import logging
import argparse
import os
import sys
sys.path.append("/Users/willbarnes/Documents/Web Development/ads")
import ads

class FetchPubs(object):
    """Class for querying ADS for publication information, compiling to YAML"""

    def __init__(self, pub_db, ads_key=os.path.join(os.environ['HOME'],'.ads/dev_key'),  people=[], people_db='',max_pub_count_debug=1e+10):
        """Constructor for FetchPubs class"""
        self.journal_name_keywords = ['Astronomy', 'Astrophysics', 'Astrophysical', 'Astronomical', 'Solar', 'Royal Society','Plasmas']
        self._config_logger()
        self._set_key(ads_key)
        self.pub_db = pub_db
        self.max_pub_count_debug = max_pub_count_debug
        if people:
            self.people = people
        else:
            self.read_people(people_db)


    def _set_key(self,ads_key):
        """Set token to query ADS"""
        with open(ads_key,'r') as f:
            self.my_ads_key = f.read()
        f.close()
        ads.config.token = self.my_ads_key
        self.logger.info("Using ADS key from file %s"%ads_key)


    def _config_logger(self):
        """Configure logger instance"""
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        self.logger.addHandler(ch)

    def read_people(self,people_db):
        """Parse YAML config file containing author information"""
        with open(people_db,'r') as f:
            people = yaml.load(f)
        self.people = []
        for p in people:
            try:
                self.people += p['pub_name']
                [self.logger.info("Adding author: %s"%pn) for pn in p['pub_name']]
            except KeyError:
                self.logger.exception("No pub name found for %s"%p['name'])


    def query_db(self):
        """Query ADS for publications by all self.people"""
        #Initialize structure to hold all publications
        self.top_level_pubs = dict()
        #Query db for all authors
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
                self.top_level_pubs[a].append({'title':t.title, 'author':t.author, 'rs_author':tmp_rsp_auth, 'year':t.year, 'pub':t.pub, 'bibcode':t.bibcode, 'property':t.property, 'volume':t.volume, 'page':t.page})
                self.logger.debug("Storing paper: %s"%t.title)
                #pub counts for debugging
                pub_count += 1
                if pub_count >= self.max_pub_count_debug:
                    self.logger.debug("Breaking at pub count %d for debugging."%self.max_pub_count_debug)
                    break


    def flatten_and_sort(self):
        """Flatten publication list and sort by year"""
        #Flatten database
        flat_pubs = []
        for a in self.people:
            flat_pubs += self.top_level_pubs[a]
        #Remove duplicates
        #unique_pubs_set = set(tuple(fp.items()) for fp in flat_pubs)
        #flat_pubs = [dict(ups) for ups in unique_pubs_set]
        #TODO: can't use set on nested dict; find a better way to remove duplicates
        #Sort by year (newest on top)
        self.flat_pubs = sorted(flat_pubs, key=lambda k: k['year'], reverse=True)


    def filter_pubs(self,paper):
        """Filter publication list"""
        #leave out older papers
        if int(paper.year) < 1995:
            check_flag = False
            return False

        #Check  the journal name
        check_flag = False
        for key in self.journal_name_keywords:
            try:
                if key in paper.pub:
                    check_flag = True
                    break
            except TypeError:
                pass

        if not check_flag:
            return check_flag

        #Check if refereed publication
        if 'NOT REFEREED' in paper.property:
            check_flag = False

        return check_flag


    def pubs2yaml(self):
        """Print publication list to YAML config file"""
        #Check for empty publication list
        if not self.flat_pubs:
            self.logger.warning("Printing empty publiction list to %s. Set publication list with self.flatten_and_sort()"%self.pub_db)
        #Print publication list to YAML file
        self.logger.info("Printing publication list to %s"%self.pub_db)
        with open(self.pub_db,'w') as yf:
            yf.write(yaml.dump(self.flat_pubs,default_flow_style=False))
        yf.close()



def main():
    #Parse command line arguments
    parser = argparse.ArgumentParser(description='Query ADS database for publications from the Rice Solar Physics Research Group')
    parser.add_argument("-k","--ads_key",help="Path to file containing ADS key needed to query database")
    parser.add_argument("-d","--pub_db",help="YAML file to write publication entries to")
    parser.add_argument("-p","--people_db",help="YAML file containing author info")
    args = parser.parse_args()
    #Instantiate publication fetcher class
    pub_finder = FetchPubs(args.pub_db, people=['Bradshaw, S. J.','Bradshaw, Stephen'], people_db=args.people_db, ads_key=args.ads_key)
    #Query database
    pub_finder.query_db()
    #Flatten and sort publications
    pub_finder.flatten_and_sort()
    #Print publications to YAML
    pub_finder.pubs2yaml()

if __name__=='__main__':
    main()
