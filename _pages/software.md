---
layout: page
permalink: /Software
title: Software
---
{% for sw in site.data.software %}
  <h2>{{ sw.name }}
  <a href="{{ sw.url }}"><i class="fa fa-github fa-lg"></i></a>
  {% if sw.docs != null %}
    <a href="{{ sw.docs }}"><i class="fa fa-book fa-lg"></i></a>
  {% endif %}
  </h2>
  <p>{{ sw.description | markdownify }}</p>
{% endfor %}
