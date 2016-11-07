---
layout: default
permalink: /Publications
title: Publications
---
{% for year in site.data.publications.years %}
<h3>{{ year }}</h3>
<div class="list-group">
  {% for paper in site.data.publications.pubs %}
  {% if paper.year contains year %}
  <a href="http://adsabs.harvard.edu/abs/{{ paper.bibcode }}" class="list-group-item list-group-item-action">
    <span class="badge">{{ paper.citation_count }}</span>
    <h5 class="list-group-item-heading">{{ paper.title }}</h5>
    <p class="list-group-item-text">{% for au in paper.author %}{% if paper.rs_author contains au %}<strong>{{ au }}</strong>, {% else %}{{ au }}, {% endif %}{% endfor %}
    {{ paper.pub }}</p>
  </a>
  {% endif %}
  {% endfor %}
</div>
{% endfor %}
