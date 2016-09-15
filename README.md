# Rice Solar Physics Group Webpage
[![Build Status](https://travis-ci.org/rice-solar-physics/group_webpage.svg?branch=master)](https://travis-ci.org/rice-solar-physics/group_webpage)

This webpage is hosted [here](http://solar.rice.edu).

## Installing Locally
To build and test this webiste locally, you'll first need to install [Jekyll](https://jekyllrb.com/), the static site generator that's used to generate all of the HTML from the Markdown files. If you'd like to autogenerate the publication list, you'll also need to install [Python](https://www.python.org/) and the [ADS package](https://github.com/andycasey/ads).

To grab the website and start the Jekyll server,
```Shell
$ git clone https://github.com/rice-solar-physics/group_webpage.git
$ cd group_webpage
$ jekyll serve
```
Navigate to `localhost:4000` in your web browser to see the site. Refresh the page to see your edits. Alternatively, you can edit/add pages as desired just using the GUI tools in the GitHub web app.

## Adding Content
If you'd like to add a post to the "news reel" on the main page, add a file in the [`_posts/`](_posts/) directory using the naming convention `{yyyy}-{mm}-{dd}-{a_short_title}.md`. This automatically sets the timestamp of the post. The first four lines of your post file should be,
```
---
layout: post
title: A Title for Your Post
---
```
Then, add any content you'd like using [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) syntax or vanilla HTML. Currently, this build uses the [kramdown](http://kramdown.gettalong.org/) Markdown parser.

To edit any of the information in the pages (e.g. People, Software), please do so in the corresponding YAML file in the [`_data/`](_data/) directory. Only edit the files in [`_pages/`](_pages/) if you'd like to change the actual layout of the page itself. Jekyll uses the [liquid templating language](https://shopify.github.io/liquid/) to avoid overly verbose Markdown files.

## Build Process and Deployment
At every commit to the master branch, a build is triggered on [Travis CI](https://travis-ci.org/rice-solar-physics/group_webpage), a continuous integration system. During this build, the publication list is generated (via [`scripts/fetch_pubs.py`](scripts/fetch_pubs.py)), Jekyll generates the HTML from the Markdown posts and pages, and the files are copied over to the Rice server where they are visible at [`solar.rice.edu`](http://solar.rice.edu). Test locally to make sure the build isn't broken before pushing up to `master`. Otherwise, your changes may not show up. If you're having touble getting the site to build after making your changes, you can inspect the build log on [Travis](https://travis-ci.org/rice-solar-physics/group_webpage).

## Design
Rice Solar Physics research group webpage based on the [Hyde Jekyll template](https://github.com/poole/hyde) with some minor modifications made using [Twitter Bootstrap](http://getbootstrap.com/2.3.2/).
