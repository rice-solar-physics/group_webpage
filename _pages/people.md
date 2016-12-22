---
layout: default
permalink: /People
title: People
notitle: true
---
{% comment %}Hardcoding is bad!{% endcomment %}
{% comment %} Set profile picture width {% endcomment %}
{% assign biopic_width = 200 %}
{% comment %} Set number of people per row {% endcomment %}
{% assign num_per_row = 4 %}
{% comment %} Set width of person column {% endcomment %}
{% assign col_width = 12 | divided_by: num_per_row %}
{% comment %} Sort current people alphabetically {% endcomment %}
{% assign sortedpeople = site.data.people | sort: 'last_name' %}
{% comment %} Sort alumni by year, newest on top {% endcomment %}
{% assign sortedpeople_year = site.data.people | sort: 'year' | reverse %}
<div class="container-fluid">
  {% for role in site.roles %}
  {% if role.key != 'alum' %}
  {% for person in sortedpeople%}
  {% if person.role == role.key %}
  {% if person.index0 | modulo:num_per_row == 0 %}
  <div class="row">
  {% endif %}
  <div class="col-lg-{{ col_width }}">
  <div class="card" style="border:0;box-shadow:none">
    {% if person.image != null %}
    <img class="card-img-top img-fluid rounded-circle" src="{{site.baseurl}}{{person.image}}" style="width:{{ biopic_width }}px"/>
    {% else %}
    <img class="card-img-top img-fluid rounded-circle" src="http://placehold.it/{{ biopic_width }}x{{ biopic_width }}?text=no+picture" />
    {% endif %}
    <div class="card-block text-xs-center">
      {% if person.webpage != null %}
      <a href="{{ person.webpage }}">
      {% endif %}
      <h5 class="card-title">{{ person.first_name }} {{ person.last_name}}</h5>
      {% if person.webpage != null %}
      </a>
      {% endif %}
      <p class="card-text text-muted">{{ role.name }}</p>
    </div>
  </div>
  </div>
  {% if person.index0 | plus:1 | modulo:num_per_row == 0 %}
  </div>
  {% endif %}
  {% endif %}
  {% endfor %}
  {% else %}
  <h3>{{ role.name }}</h3>
  {% for person in sortedpeople_year %}
  {% if person.role == role.key %}
  <div class="col-xs-12">
    <h5 style="display:inline-block">{{ person.first_name }} {{ person.last_name }}</h5>
    <span>{% if person.degree != null and person.year != null %}{{ person.degree }} ({{ person.year }}){% endif %}{% if person.position != null %}{{ person.position }}{% endif %}</span>
  </div>
  {% endif %}
  {% endfor %}
  {% endif %}
  {% endfor %}
</div>
