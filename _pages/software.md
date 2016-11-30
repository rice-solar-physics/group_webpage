---
layout: default
permalink: /Software
title: Software
notitle: true
---
<div class="list-group">
  {% for sw in site.data.software %}
  <div class="row list-group-item">
    <div class="row">
    <div class="col-md-10" style="vertical-align:middle">
      <h4 class="list-group-item-heading">{{ sw.name }}</h4>
    </div>
    <div class="col-md-2" style="text-align:right;vertical-align:middle">
      <a href="{{ sw.url }}"><i class="fa fa-github fa-2x"></i></a>
      {% if sw.docs != null %}
      <a href="{{ sw.docs }}"><i class="fa fa-book fa-2x"></i></a>
      {% endif %}
    </div>
    </div>
    <p class="list-group-item-text">{{ sw.description | markdownify }}</p>
  </div>
  {% endfor %}
</div>
