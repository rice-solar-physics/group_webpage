---
layout: default
permalink: /Research
title: Research
notitle: true
---
{% for res in site.data.research %}
<div class="row">
  <h4>{{ res.name }}</h4>
  <div class="col-md-3">
  {% if res.images != null %}
  {% for image in res.images %}
    <div class="card">
    <img class="card-img-top img-responsive" src="{{ site.baseurl }}{{ image }}"/>
    </div>
  {% endfor %}
  {% endif %}
  </div>
  <div class="col-md-9">
  <p>{{ res.description | markdownify }}</p>
  </div>
</div>
{% endfor %}
