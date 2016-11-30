---
layout: default
permalink: /Publications
title: Publications
notitle: true
---
{% for year in site.data.publications.years %}
<h4>{{ year }}</h4>
<div class="list-group">
  {% for paper in site.data.publications.pubs %}
  {% if paper.year contains year %}
  <a href="http://adsabs.harvard.edu/abs/{{ paper.bibcode }}" class="list-group-item list-group-item-action">
    <span class="tag tag-pill tag-primary float-xs-right">{{ paper.citation_count }}</span>
    <h6 class="list-group-item-heading">{{ paper.title }}</h6>
    <p class="list-group-item-text">{% for au in paper.author %}{% if paper.rs_author contains au %}<strong>{{ au }}</strong>, {% else %}{{ au }}, {% endif %}{% endfor %}
    {{ paper.pub }}</p>
  </a>
  {% endif %}
  {% endfor %}
</div>
{% endfor %}
