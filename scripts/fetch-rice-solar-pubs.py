#name: fetch-rice-solar-pubs.py
#author: Will Barnes
#date: 15 January 2016
#description: Query ADS database for publications from Rice Solar Physics research group

#Import needed packages
import argparse
import sys
import yaml

#Parse cl args
#Parse command line arguments
parser = argparse.ArgumentParser(description='Query ADS database for publications from the Rice Solar Physics Research Group')
parser.add_argument("-p","--ads_path",help="Path to ads query module")
parser.add_argument("-k","--ads_key",help="Path to file containing ADS key needed to query database")
parser.add_argument("-d","--pub_db",help="YAML file to write publication entries to")
args = parser.parse_args()

#Import ads query module
sys.path.append(args.ads_path)
import ads

#Read and configure ads token
with open(args.ads_key,'r') as f:
    my_ads_key = f.read()
f.close()
ads.config.token = my_ads_key

#Authors
rsp_authors = ['Bradshaw, S. J.']

#Initialize structure to hold all publications
top_level_pubs = dict()

#Query db for all authors
for a in rsp_authors:
    tmp = list(ads.SearchQuery(author=a))
    top_level_pubs[a] = []
    for t in tmp:
        #Flag Rice authors
        tmp_rsp_auth = []
        for ta in t.author:
            if ta in rsp_authors:
                tmp_rsp_auth.append(ta)
        top_level_pubs[a].append({'name':t.title,'author':t.author,'rs_author':tmp_rsp_auth,
        'year':t.year,'pub':t.pub,'bibcode':t.bibcode,'property':t.property,
        'volume':t.volume,'page':t.page})

#Flatten database (one list of dictionaries) and TODO:remove duplicates
flat_pubs = top_level_pubs[rsp_authors[0]]
#TODO:Sort by year (newest on top)

#TODO: sort out conference papers from articles, int separate files maybe

#TODO: flag Rice-affiliated authors

#Print to YAML file
with open(args.pub_db,'w') as yf:
    yf.write(yaml.dump(flat_pubs,default_flow_style=False))
yf.close()
