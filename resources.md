---
layout: page
title: Resources
---

<!--{% include resources.html %}-->
<dl>
  {% for res in site.data.resources %}
    <dt><a href="{{res.link}}">{{res.name}}</a></dt>
    <dd>{{res.description}}</dd>
  {% endfor %}
</dl>
