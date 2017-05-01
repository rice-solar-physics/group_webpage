---
layout: workshop
title: Modeling the Magnetic Interactions between Stars and Planets
permalink: mmisp-2017/index
workshop_name: mmisp-2017
notitle: true
contacts:
- first_name: David
  last_name: Alexander
  role: Director, Rice Space Institute
  phone: 713.348.3633
  email: dalex@rice.edu
- first_name: Treasure
  last_name: Wilson
  role: Administrator, Rice Space Institute
  phone: 713.348.2068 
  email: treasure.wilson@rice.edu
---
<div class="text-xs-center">
<h4 class="text-muted">An NSF Funded Invitation-only Workshop</h4>
<h1>{{page.title}}</h1>
<h3 class="text-muted">May 15-16 2017</h3>
<h3 class="text-muted">Rice University, Brockman Hall for Physics, Room 200</h3>
</div>

<figure class="figure">
    <img src="{{ site.baseurl }}images/brockman.png" class="figure-img img-responsive img-thumbnail mx-auto d-block" style="max-width:85%;max-height:auto;">
    <figcaption class="figure-caption text-xs-center">Brockman Hall for Physics, image courtesy of <a href="http://moranstudio.com/">Michael Moran</a></figcaption>
</figure>

<p class="lead text-justify">
Welcome to the workshop on Modeling the Magnetic Interactions between Stars and Planets at Rice University! The purpose of this workshop is to discuss how our understanding of the magnetic interactions between the Sun and solar system planets can be applied to solar-planet interactions in exoplanet systems. The focus will be on relevant modeling and observational verification. The workshop will be focused on sharing knowledge and ideas to identify specific areas of study, the current state of the observations, specific model/observational comparisons and priorities, and on possibly developing joint efforts.
</p>

<h3>Directions</h3>
<ul class="list-unstyled lead">
<li><a href="http://www.rice.edu/maps/getdirections.html">Directions to Rice University</a></li>
<li><a href="http://rsi.rice.edu/files/2016/11/Rice-University-Color-Campus-Map-Brockman-edited-24uch5w.jpg">Rice University Campus Map</a></li>
</ul>

<h3>Contacts</h3>
<div class="container">
{% for contact in page.contacts %}
<div class="row">
<div class="col-sm-3 lead">
{{ contact.first_name }} {{ contact.last_name }}
</div>
<div class="col-sm-5 lead text-muted">
{{ contact.role }}
</div>
<div class="col-sm-4 lead">
<i class="fa fa-phone" aria-hidden="true"></i>  {{ contact.phone }}
<a href="mailto:{{ contact.email }}"><i class="fa fa-envelope" aria-hidden="true"></i></a>
</div>
</div>
{% endfor %}
</div>
