---
layout: default
permalink: /Research
title: Research
notitle: true
---
<div class="card-columns">
  {% for res in site.research %}
  <div class="card">
    <div class="card-block">
      <a href="{{ res.url }}">
      <h4 class="card-title">{{ res.title }}</h4>
      </a>
      <p class="card-text">{{ res.short_description }}</p>
    </div>
    <div class="card-footer">
      {% for people in res.people %}
      {% for subpeople in site.data.people %}
      {% if people == subpeople.last_name and subpeople.image != null%}
      <img class="card-img-top rounded-circle pull-right" src="{{ site.baseurl }}{{ subpeople.image }}" style="width:35px;margin-right:5px" />
      {% endif %}
      {% endfor %}
      {% endfor %}
    </div>
  </div>
  {% endfor %}
</div>
