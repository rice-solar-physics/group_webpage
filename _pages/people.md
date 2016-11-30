---
layout: default
permalink: /People
title: People
notitle: true
---
{% comment %} Sort current people alphabetically {% endcomment %}
{% assign sortedpeople = site.data.people | sort: 'last_name' %}
{% comment %} Sort alumni by year, newest on top {% endcomment %}
{% assign sortedpeople_year = site.data.people | sort: 'year' | reverse %}
{% for role in site.roles %}
<div class="row">
  <h3>{{ role.name }}</h3>
  {% if role.key != 'alum' %}
  {% for person in sortedpeople %}
  {% if person.role == role.key %}
  <div class="col-lg-4">
    <div class="card" style="border:0;box-shadow:none">
      {% if person.image != null %}
      <img class="card-img-top img-fluid rounded-circle" src="{{site.baseurl}}{{person.image}}" style="width:150px"/>
      {% else %}
      <img class="card-img-top img-fluid rounded-circle" src="http://placehold.it/150x150?text=no+picture" />
      {% endif %}
      <div class="card-block">
        {% if person.webpage != null %}
        <a href="{{ person.webpage }}">
        {% endif %}
        <h5 class="card-title">{{ person.first_name }} {{ person.last_name}}</h5>
        {% if person.webpage != null %}
        </a>
        {% endif %}
      </div>
    </div>
  </div>
  {% endif %}
  {% endfor %}
  {% else %}
  {% for person in sortedpeople_year %}
  {% if person.role == role.key %}
  <div class="col-xs-12">
    <h5 style="display:inline-block">{{ person.first_name }} {{ person.last_name }}</h5>
    <span>{% if person.degree != null and person.year != null %}{{ person.degree }} ({{ person.year }}){% endif %}{% if person.position != null %}{{ person.position }}{% endif %}</span>
  </div>
  {% endif %}
  {% endfor %}
  {% endif %}
</div>
{% endfor %}
