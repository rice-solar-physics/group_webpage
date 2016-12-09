---
layout: default
permalink: /Software
title: Software
notitle: true
---
{% for sw in site.data.software %}
<div class="card">
  <div class="card-header">
    <div class="pull-right">
      <a href="{{ sw.url }}"><i class="fa fa-github fa-2x"></i></a>
      {% if sw.docs != null %}
      <a href="{{ sw.docs }}"><i class="fa fa-book fa-2x"></i></a>
      {% endif %}
    </div>
    <h4>{{ sw.name }}</h4>
  </div>
  <div class="card-block">
    <p class="card-text">{{ sw.description | markdownify }}</p>
  </div>
</div>
{% endfor %}
