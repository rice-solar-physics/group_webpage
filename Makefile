PYTHON=python
ADSKEY=$(ADS_KEY)
RUPASS=$(RU_PASS)
RUUSER=$(RU_USER)
MOUNTDIR=$(MOUNT_DIR)

all: build

pubs:
	@$(PYTHON) scripts/fetch_pubs.py -k $(ADSKEY) -f _data/publications.yml -p _data/people.yml

pubs_pr:
	touch _data/publications.yml

_build:
	bundle exec jekyll build

build: pubs _build

build_pr: pubs_pr _build

netlify_install:
	pip install ads
	pip install PyYaml

netlify: netlify_install build

deploy: build
	sshpass -p $(RUPASS) rsync -a --delete _site/ $(RUUSER)@wtb2.rice.edu:$(MOUNTDIR)

clean:
	rm _data/publications.yml
	rm -r _site
