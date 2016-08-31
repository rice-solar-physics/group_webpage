---
layout: page
permalink: /People
title: People
---
{% for category in site.data.people %}
<div class="row">
  <h2>{{ category.name }}</h2>
  {% for person in category.people %}
  <div class="col-sm-6 col-md-5 col-lg-5">
    <div class="thumbnail">
      {% if person.image != null %}
      <img class="img-responsive" src="{{site.baseurl}}{{person.image}}"/>
      {% else %}
      <img class="img-responsive" src="http://placehold.it/500x500?text=no+picture"/>
      {% endif %}
      <div class="caption">
        {% if person.webpage != null %}
        <p class="lead" style="text-align:center"><a href="{{ person.webpage }}">{{ person.name }}</a></p>
        {% else %}
        <p class="lead" style="text-align:center">{{ person.name }}</p>
        {% endif %}
        {% if category.name == "Alumni" %}
        <ul>
        <li>{{ person.degree }} ({{ person.year }})</li>
        <li>{{ person.position }}</li>
        <li>{{ person.institution }}, {{ person.location }}</li>
        </ul>
        {% endif %}
      </div>
    </div>
  </div>
  {% endfor %}
</div>
{% endfor %}
