# Rice Solar Physics Group Webpage
[![Build Status](https://travis-ci.org/rice-solar-physics/group_webpage.svg?branch=master)](https://travis-ci.org/rice-solar-physics/group_webpage)

This webpage is hosted [here](http://solar.rice.edu).

# Installing Locally
To build and test this webiste locally, you'll first need to install [Jekyll](https://jekyllrb.com/), the static site generator that's used to generate all of the HTML from the Markdown files. If you'd like to autogenerate the publication list, you'll also need to install [Python](https://www.python.org/) and the [ADS package](https://github.com/andycasey/ads).

To grab the website and start the Jekyll server,
```Shell
$ git clone https://github.com/rice-solar-physics/group_webpage.git
$ cd group_webpage
$ jekyll serve
```
Navigate to `localhost:4000` in your web browser to see the site. Refresh the page to see your edits. Alternatively, you can edit/add pages as desired just using the GUI tools in the GitHub web app.

## Adding Content

## Build Process and Deployment
At every commit to the master branch, a build is triggered on [Travis CI](), a continuous integration system. During this build, the publication list is generated (via [`scripts/fetch_pubs.py`](#/scripts/fetch_pubs.py)), Jekyll generates the HTML from the Markdown posts and pages, and the files are copied over to the Rice server where they are visible at [`solar.rice.edu`](http://solar.rice.edu). Test locally to make sure the build isn't broken before pushing up to `master`. Otherwise, your changes may not show up.


## Design
Rice Solar Physics research group webpage based on the [Hyde Jekyll template](https://github.com/poole/hyde) with some minor modifications made using [Twitter Bootstrap](http://getbootstrap.com/2.3.2/).
