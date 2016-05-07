---
layout: page
permalink: /Research
title: Research
---
<!--<div class="container">-->
{% for res in site.data.research %}
  <!--<div class="row" style="align-items:center">-->
  <h2>{{ res.name }}</h2>
  <div class="col-md-4">
  {% for image in res.images %}
    <img src="{{ site.baseurl }}{{ image }}"/>
  {% endfor %}
  </div>
  <div class="col-md-8">
  <p>{{ res.description | markdownify }}</p>
  </div>
  <!--</div>-->
{% endfor %}
<!--</div>-->
