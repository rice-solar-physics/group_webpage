---
layout: default
permalink: /Resources
title: Resources
---
<dl>
  {% for res in site.data.resources %}
    <dt><a href="{{res.link}}">{{res.name}}</a></dt>
    <dd>{{res.description}}</dd>
  {% endfor %}
</dl>
