---
layout: page
permalink: /Research
title: Research
---

<div class="post">
{% for res in site.research %}
    <h2 class="post-title">{{ res.title }}</h2>
    <div class="col-md-4">
      {% for image in res.images %}
        <img src="{{ site.baseurl }}{{ image }}"/>
      {% endfor %}
    </div>
    <div class="col-md-8">
      {{ res.content }}
    </div>
{% endfor %}
</div>
