---
layout: default
permalink: /Research
title: Research
---
<div class="row">
{% for res in site.data.research %}
  <h2>{{ res.name }}</h2>
  <div class="col-md-4">
  {% if res.images != null %}
  {% for image in res.images %}
    <div class="thumbnail">
    <img class="img-responsive" src="{{ site.baseurl }}{{ image }}"/>
    </div>
  {% endfor %}
  {% endif %}
  </div>
  <div class="col-md-8">
  <p>{{ res.description | markdownify }}</p>
  </div>
{% endfor %}
</div>
