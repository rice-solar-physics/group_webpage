---
layout: default
permalink: /Resources
title: Resources
notitle: false
---
<div class="list-group">
  {% for res in site.data.resources %}
  <a href="{{res.link}}" class="list-group-item list-group-item-action">
  <h4 class="list-group-item-heading">{{res.name}}</h4>
  <p class="list-group-item-text">{{res.description}}</p>
  </a>
  {% endfor %}
</div>
