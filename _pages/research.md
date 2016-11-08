---
layout: default
permalink: /Research
title: Research
notitle: true
---
{% for res in site.data.research %}
<div class="row">
  <h2>{{ res.name }}</h2>
  <div class="col-md-3">
  {% if res.images != null %}
  {% for image in res.images %}
    <div class="thumbnail">
    <img class="img-responsive" src="{{ site.baseurl }}{{ image }}"/>
    </div>
  {% endfor %}
  {% endif %}
  </div>
  <div class="col-md-9">
  <p>{{ res.description | markdownify }}</p>
  </div>
</div>
{% endfor %}
