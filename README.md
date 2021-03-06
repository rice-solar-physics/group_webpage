# Rice Solar Physics Group Webpage
[![Build Status](https://travis-ci.org/rice-solar-physics/group_webpage.svg?branch=master)](https://travis-ci.org/rice-solar-physics/group_webpage)

## Installing Locally
To build and test this website locally, you'll first need to install [Jekyll](https://jekyllrb.com/), the static site generator that's used to generate all of the HTML from the Markdown files, and [Bundler](http://bundler.io/). If you'd like to autogenerate the publication list, you'll also need to install [Python](https://www.python.org/) and the [ADS package](https://github.com/andycasey/ads).

To grab the website and start the Jekyll server,
```Shell
$ git clone https://github.com/rice-solar-physics/group_webpage.git
$ cd group_webpage
$ bundle install
$ bundle exec jekyll serve
```
Navigate to `localhost:4000` in your web browser to see the site. Refresh the page to see your edits. Alternatively, you can edit/add pages as desired just using the GUI tools in the GitHub web app.

## Adding Content
You can edit this site by either editing the files directly in the GitHub webapp or cloning the whole repository and editing them locally. Either way, please fork this repository first and then submit a pull request in order to make changes.

### Posts
If you'd like to add a post to the "news reel" on the main page, add a file in the [`_posts/`](_posts/) directory using the naming convention `{yyyy}-{mm}-{dd}-{a_short_title}.md`. This automatically sets the timestamp of the post. The first several lines of your post must contain the following metadata:
```yaml
---
layout: post
title: A Title for Your Post
shortnews: true
icon: newspaper-o
---
The content of your post goes here...
```
If you'd like your post to appear on the front page as a link, set `shortnews: false`. Set the `icon` option as any of the [Font Awesome icons](http://fontawesome.io/icons/). If you don't include the `shortnews` or `icon` attributes, they will default to `false` and `newspaper-o`, respectively.

Then, add any content you'd like using [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) syntax or vanilla HTML. Currently, this build uses the [redcarpet](https://github.com/vmg/redcarpet) Markdown parser.

### People
To add information about a new group member, add an entry to the [`_data/people.yml`](_data/people.yml). The only required pieces of information are `first_name`, `last_name`, and `role`. `role` must be one of they keys listed under `roles` in [`_config.yml`](_config.yml).

### Research
To edit any of the research topic pages, make all of the changes in the appropriate Markdown file in the `research/` directory. You can write either Markdown or HTML. When adding images, put those in the `images/` directory and link to them appropriately.

When adding a new research topic, add a new Markdown file in the `research/` directory and it will appear as a card on the "Research" page. Each file should include the following metadata,
```yaml
---
layout: default
title: A New Research Topic
short_description: Here is a short summary that will show up on the card
people:
  - last_name_of_person_a_working_on_this_project
  - last_name_of_person_b_working_on_this_project
---
The full description of the project should go here...
```

### Other Metadata
To edit any of the information in the other pages (e.g. Software, Resources), please do so in the corresponding YAML file in the [`_data/`](_data/) directory. Only edit the files in [`_pages/`](_pages/) if you'd like to change the actual layout of the page itself. Jekyll uses the [liquid templating language](https://shopify.github.io/liquid/) to avoid overly verbose Markdown files.

## Build Process and Deployment
At every commit to the master branch, a build is triggered on [Travis CI](https://travis-ci.org/rice-solar-physics/group_webpage), a continuous integration system. During this build, the publication list is generated (via [`scripts/fetch_pubs.py`](scripts/fetch_pubs.py)), Jekyll generates the HTML from the Markdown posts and pages, and the files are copied over to the Rice server where they are visible at [`solar.rice.edu`](http://solar.rice.edu). Test locally to make sure the build isn't broken before pushing up to `master`. Otherwise, your changes may not show up. If you're having touble getting the site to build after making your changes, you can inspect the build log on [Travis](https://travis-ci.org/rice-solar-physics/group_webpage).

## Design
Rice Solar Physics research group webpage based on the [research group webpage template provided by the UW Sampa group](https://github.com/uwsampa/research-group-web) and the [UW Sampa group webpage](http://sampa.cs.washington.edu/). Some minor modifications made using [Twitter Bootstrap](https://getbootstrap.com/).
