---
layout: default
permalink: /Resources
title: Resources
notitle: true
---
<div class="list-group">
  {% assign resources = site.data.resources | sort: 'name' %}
  {% for res in resources %}
  <a href="{{res.link}}" class="list-group-item list-group-item-action">
  <h5 class="list-group-item-heading">{{res.name}}</h5>
  <p class="list-group-item-text">{{res.description}}</p>
  </a>
  {% endfor %}
</div>
