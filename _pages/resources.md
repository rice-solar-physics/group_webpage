---
layout: default
permalink: /Resources
title: Resources
---
{% for res in site.data.resources %}
<h4><a href="{{res.link}}">{{res.name}}</a></h4>
<p>{{res.description}}</p>
{% endfor %}
