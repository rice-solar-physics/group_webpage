---
layout: workshop
title: Agenda
permalink: mmisp-2017/Agenda
workshop_name: mmisp-2017
notitle: true
agenda:
- date: Sunday May 14
  events:
  - time: 5:00 - 7:00 PM
    name: Reception, Martel College, Magister House (Building 50 on <a href="http://rsi.rice.edu/files/2016/11/Rice-University-Color-Campus-Map-Brockman-edited-24uch5w.jpg">campus map</a>)
- date: Monday May 15
  events:
  - time: 8:30 - 9:00 AM
    name: Breakfast
  - time: 9:00 - 9:15 AM
    name: Statement and Introduction of Scope (Alexander and Cohen)
  - time: 9:15 - 10:30 AM
    name: Stellar Activity
    chair: Johns-Krull
    talks:
    - time: 9:15 AM
      name: "PTFO8-8695: A Young Planet Feeding Material its Host Star's Magnetosphere"
      speaker: Chris Johns-Krull
    - time: 9:30 AM
      name: "Photospheric magnetic fields: the solar perspective"
      speaker: Marc DeRosa
    - time: 9:45 AM
      name: Scaling Solar Activity to Sun-like Stars
      speaker: David Alexander
    - time: 10:00 AM
      name: Calibrating a Solar Wind Model and Extending it to other Solar-like Stars
      speaker: Victor Réville
    - time: 10:15 AM
      name: Coronal Dimmings as a Proxy for Stellar CMEs
      speaker: Meng Jin
  - time: 10:30 - 11:00 AM
    name: Coffee Break
  - time: 11:00 AM - 12:45 PM
    name: Star-planet Interactions
    chair: Cohen
    talks:
    - time: 11:00 AM
      speaker: Scott Wolk
      name: "Observable Impacts of Exoplanets on Stellar Hosts: An X-Ray Perspective"
    - time: 11:15 AM
      name: Ongoing and Future Observational Efforts to Detect Planets via Star-planet Interactions
      speaker: Andrea Isella
    - time: 11:30 AM
      name: Evidence for Star-planet Interactions in the MUSCLES Treasury Survey Data
      speaker: Jeff Linsky
    - time: 11:45 AM
      name: Searching for Low-Frequency Radio Emission from Stars and Exoplanets
      speaker: Jason Ling
    - time: 12:00 PM 
      name: The Impact of Stellar Activity on High Energy Exoplanet Transits
      speaker: Joe Llama
    - time: 12:15 PM
      name: Planet-star interaction (particle-in-cell kinetic code)
      speaker: Lofti Ben-Jaffel
    - time: 12:30 PM
      name: Radio observational signatures of stellar coronal mass ejections and exoplanet magnetospheres
      speaker: Greg Hallinan
  - time: 12:45 - 2:30 PM
    name: Lunch (provided)
  - time: 2:30 - 4:00 PM
    name: Magnetospheres and Atmospheres
    chair: Toffoletto
    talks:
    - time: 2:30 PM
      name: Exomoons and Magnetic Fields 
      speaker: David Kipping
    - time: 2:45 PM
      name: HST Observations of the Extended Upper-atmospheres and Magnetospheres of Exoplanets
      speaker: Gilda Ballester
    - time: 3:00 PM
      name: Magnetospheric and Ionospheric Response to Strong Stellar Activity
      speaker: Anthony Sciola
    - time: 3:15 PM
      name: The Largest Possible Geomagnetic Storm
      speaker: Frank Toffoletto
    - time: 3:30 PM
      name: Atmospheric Consequences for Planets Residing in Sub-Alfvenic Stellar Wind
      speaker: Ofer Cohen
    - time: 3:45 PM
      name: Extreme Events from Active Stars and their Effects on Magnetospheres and Ionospheres of Terrestrial Type Planets
      speaker: Vladimir Airapetian
  - time: 4:00 - 4:30 PM
    name: Coffee Break
  - time: 4:30 - 5:30 PM
    name: Planetary Analogs
    chair: Alexander
    talks:
    - time: 4:30 PM
      name: Atmospheric Ion Loss at Mars and Exoplanets
      speaker: Chaunfei Dong
    - time: 4:45 PM
      name: Ionospheric Outflow and Atmospheric Escape at Earth and Exoplanets
      speaker: Alex Glocer
    - time: 5:00 PM
      name: Volatile Fractionation during Early Differentiation of Terrestrial Planets
      speaker: Raj Dasgupta
    - time: 5:15 PM
      name: TBA
      speaker: Adrian Lenardic
  - time: 7:30 - 9:30 PM
    name: Group Dinner at Pico's (Shuttle will be provided)
- date: Tuesday May 16
  events:
  - time: 8:30 - 9:00 AM
    name: Breakfast
  - time: 9:00 - 9:20 AM
    name: Rice’s Magnetospheric / Ionospheric Modeling Capability (Toffoletto)
  - time: 9:20 - 10:30 AM
    name: "Group Discussion: key ideas for collaboration"
  - time: 10:30 - 11:00 AM
    name: Coffee Break
  - time: 11:00 AM - 12:30 PM
    name: "Group Discussion: moving forward, plans and actions"
  - time: 12:30 - 2:00 PM
    name: Lunch and adjourn
  - time: 2:00 - 5:00 PM
    name: Informal Discussions (optional)

---
<div class="alert alert-danger" role="alert">
  All talks will be limited to 12 minutes plus 3 minutes for questions
</div>

{% for day in page.agenda %}
<div class="card">
<h3 class="card-header">{{ day.date }}</h3>
<div class="list-group list-group-flush">
{% for event in day.events %}
  <{% if event.talks != null %}a{% else %}li{% endif %} class="list-group-item justify-content-between" data-toggle="collapse" href="#talks{{ forloop.index }}">
  <div class="row lead">
  <div class="col-sm-3">
  <b>{{ event.time }}</b>
  </div>
  <div class="col-sm-9 text-sm-right">
  {{ event.name }}{% if event.chair != null %} (Chair: {{ event.chair }}){% endif %}
  </div>
  </div>
  {% if event.talks != null %}
  <div class="collapse" id="talks{{ forloop.index }}">
  {% for talk in event.talks %}
    <a href="#" class="list-group-item list-group-item-action">
    <div class="row">
      <div class="col-sm-2">
        <b>{{ talk.time }}</b>
      </div>
      <div class="col-sm-10 text-sm-right">
        {{ talk.name }}<br/><p class="text-muted">{{ talk.speaker }}</p>
      </div>
    </div>
    </a>
  {% endfor %}
  </div>
  {% endif %}
  </{% if event.talks != null %}a{% else %}li{% endif %}>
{% endfor %}
</div>
</div>
{% endfor %}
