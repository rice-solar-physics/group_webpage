---
layout: page
title: Research
---

<div class="post">
{% for res in site.research %}
    <h2 class="post-title">{{ res.title }}</h2>
    <div class="col-md-4">
      <img src="{{ site.baseurl }}{{ res.image }}" style="border: 10px solid #000000;"/>
    </div>
    <div class="col-md-8">
      {{ res.content }}
    </div>
{% endfor %}
</div>
