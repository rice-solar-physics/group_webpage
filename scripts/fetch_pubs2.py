"""
Retrieve publication list for Rice solar physics research group from ADS
"""
import os
import datetime
import yaml
import ads

# TODO: Add commandline arguments for input/output files


def accept_publication(pub):
    """
    Reject some publications. Add any conditions here.
    """
    if 'NOT REFEREED' in pub.property:
        return False
    if len(pub.author) > 10:
        return False
    return True


# parse people file for pub names
with open('_data/people.yml', 'r') as f:
    people = yaml.load(f)
people = [pn for p in people if 'pub_name' in p for pn in p['pub_name']]

# the properties we want
properties = ['author', 'year', 'pub', 'bibcode', 'title']
other_properties = ['citation', 'pubdate', 'property']

# query for all people, Rice affiliation only
all_pubs = []
for p in people:
    query = list(ads.SearchQuery(author=p, aff='Rice', fl=properties+other_properties))
    for q in query:
        if not accept_publication(q):
            continue
        tmp = {p: q.__dict__[p] for p in properties}
        tmp['year'] = int(tmp['year'])
        tmp['rs_author'] = [a for a in q.author if a in people]
        tmp['citation_count'] = len(q.citation) if q.citation is not None else 0
        tmp['date'] = '-'.join(['01' if dt == '00' else dt for dt in q.pubdate.split('-')])
        all_pubs.append(tmp)

# sort by year
all_pubs = sorted(all_pubs, 
                  key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d'), 
                  reverse=True)

# remove duplicates by title
# FIXME: why so many duplicates?
unique_titles = []
unique_pubs = []
for ap in all_pubs:
    if ap['title'] in unique_titles:
        continue
    else:
        unique_titles.append(ap['title'])
        unique_pubs.append(ap)

all_pubs = unique_pubs

# write out to yaml file
years = sorted(list(set([int(p['year']) for p in all_pubs])), reverse=True)
all_pubs = {'pubs': all_pubs, 'years': years}
with open('_data/publications.yml','w') as f:
    f.write(yaml.dump(all_pubs, default_flow_style=False))