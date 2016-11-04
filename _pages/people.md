---
layout: default
permalink: /People
title: People
notitle: true
---
{% for role in site.roles %}
<div class="row">
<h2>{{ role.name }}</h2>
  {% for person in site.data.people %}
  <div class="col-md-{% if role.key == 'alum' or role.key == 'ressci' %}12{% else %}4{% endif %}">
  {% if person.role == role.key %}
    {% if role.key != 'alum' %}
    {% if person.image != null %}
    <img class="img-responsive img-circle" src="{{site.baseurl}}{{person.image}}" style="width:125px"/>
    {% else %}
    <img class="img-responsive img-circle" src="http://placehold.it/125x125?text=no+picture"/>
    {% endif %}
    {% if person.webpage != null %}
    <a href="{{ person.webpage }}">
    {% endif %}
    <h4>{{ person.name }}</h4>
    {% if person.webpage != null %}
    </a>
    {% endif %}
    {% else %}
    <h4 style="display:inline-block">{{ person.name }}</h4>
    <span>{% if person.degree != null and person.year != null %}{{ person.degree }} ({{ person.year }}){% endif %}{% if person.position != null %}{{ person.position }}{% endif %}</span>
    {% endif %}
  {% endif %}
  </div>
  {% endfor %}
</div>
{% endfor %}
