---
layout: page
permalink: /People
title: People
---
{% for category in site.data.people %}
<div class="row">
  <h2>{{ category.name }}</h2>
  {% for person in category.people %}
  {% if category.name != "Alumni" %}
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
      </div>
    </div>
  </div>
  {% else %}
  <ul>
  <li>{{ person.name }}{% if person.degree != null and person.year != null %}, {{ person.degree }} ({{ person.year }}){% endif %}{% if person.position != null %}, {{ person.position }}{% endif %}</li>
  </ul>
  {% endif %}
  {% endfor %}
</div>
{% endfor %}
