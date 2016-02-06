---
layout: page
title: People
---

<h2>Current Members</h2>
<ul>
  {% for person in site.data.people %}
    <h3>{{ person.name }}</h3>
    <li>{{ person.position }}</li>
    {% if person.webpage != null %}
      <li><a href="{{ person.webpage }}" >Personal Webpage</a></li>
    {% endif %}
  {% endfor %}
</ul>
<h2>Alumni</h2>
<ul>
  {% for person in site.data.alumni %}
    <h3>{{ person.name }}</h3>
    <li>{{ person.degree }} ({{ person.year }}), <em>{{ person.thesis }}</em></li>
    <li>{{ person.position }}</li>
    <li>{{ person.institution }}, {{ person.location }}</li>
  {% endfor %}
</ul>
