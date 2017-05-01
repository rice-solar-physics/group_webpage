---
layout: workshop
title: Participants
permalink: mmisp-2017/Participants
workshop_name: mmisp-2017
notitle: true
participants:
- first_name: Vladimir
  last_name: Airapetian
  affiliation: NASA Goddard Space Flight Center
- first_name: Gilda 
  last_name: Ballester
  affiliation: University of Arizona
- first_name: Lotfi
  last_name: Ben-Jaffel
  affiliation: Institut d’Astrophysique de Paris
- first_name: Ofer
  last_name: Cohen
  affiliation: University of Massachusetts, Lowell
- first_name: Marc
  last_name: DeRosa
  affiliation: Lockheed Martin Advanced Technology Center
- first_name: Chuanfei
  last_name: Dong
  affiliation: Princeton University
- first_name: Alex
  last_name: Glocer
  affiliation: NASA Goddard Space Flight Center
- first_name: Greg 
  last_name: Hallinan
  affiliation: CalTech
- first_name: Meng
  last_name: Jin		
  affiliation: Lockheed Martin Advanced Technology Center
- first_name: David 
  last_name: Kipping
  affiliation: Columbia University
- first_name: Jeff
  last_name: Linsky
  affiliation: University of Colorado
- first_name: Joe
  last_name: Llama 		
  affiliation: Lowell Observatory
- first_name: Victor
  last_name: Réville
  affiliation: CEA Saclay
- first_name: Scott
  last_name: Wolk
  affiliation: Harvard-Smithsonian Center for Astrophysics
- first_name: David
  last_name: Alexander 	
  affiliation: Rice University 
  department: Physics and Astronomy 
- first_name: Stephen
  last_name: Bradshaw
  affiliation: Rice University 
  department: Physics and Astronomy
- first_name: Anthony
  last_name: Chan
  affiliation: Rice University 
  department: Physics and Astronomy 
- first_name: Raj
  last_name: Dasgupta
  affiliation: Rice University 
  department: Earth Science
- first_name: Antoun
  last_name: Daou
  affiliation: Rice University 
  department: Physics and Astronomy
- first_name: Alison
  last_name: Farrish
  affiliation: Rice University 
  department: Physics and Astronomy
  grad_student: true
- first_name: Laura
  last_name: Flagg
  affiliation: Rice University 
  department: Physics and Astronomy
  grad_student: true
- first_name: Andrea
  last_name: Isella
  affiliation: Rice University 
  department: Physics and Astronomy
- first_name: Chris 
  last_name: Johns-Krull
  affiliation: Rice University 
  department: Physics and Astronomy 
- first_name: Cin-Ty 
  last_name: Lee
  affiliation: Rice University 
  department: Earth Science
- first_name: Adrian
  last_name: Lenardic 
  affiliation: Rice University 
  department: Earth Science
- first_name: Jason
  last_name: Ling
  affiliation: Rice University 
  department: Physics and Astronomy
  grad_student: true
- first_name: Stan
  last_name: Sazykin
  affiliation: Rice University 
  department: Physics and Astronomy
- first_name: Anthony
  last_name: Sciola
  affiliation: Rice University 
  department: Physics and Astronomy
  grad_student: true
- first_name: Frank
  last_name: Toffoletto
  affiliation: Rice University 
  department: Physics and Astronomy
---
<p class="lead"><em>Italics indicate participant is a graduate student</em></p>
{% assign sortedpeople = page.participants | sort: 'last_name' %}
<div class="list-group">
{% for person in  sortedpeople %}
    <li class="list-group-item list-group-item-action justify-content-between">
    <div class="row lead">
    <div class="col-xs-3">
    {% if person.grad_student != null %}<em>{% endif %}
    {{ person.first_name }} {{ person.last_name}}
    {% if person.grad_student != null %}</em>{% endif %}
    </div>
    <div class="col-xs-9 text-xs-right">
    {{ person.affiliation }} {% if person.affiliation == "Rice University" %}({{ person.department }}){% endif %}
    </div>
    </row>
    </li>
{% endfor %}
</div>