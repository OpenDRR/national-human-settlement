---
authorName: Natural Resources Canada
authorUrl:
dateModified: 2021-07-26
pageclass: wb-prettify all-pre
subject:
  en: [GV Government and Politics, Government services]
  fr: [GV Gouvernement et vie politique, Services gouvernementaux]
title: Zones de peuplement et dangers naturels au Canada
lang: fr
altLangPage: ../en
nositesearch: true
nomenu: true
nofooter: true
breadcrumbs:
  - title: "OpenDRR"
    link: "https://www.github.com/OpenDRR/"
  - title: "Téléchargements de OpenDRR"
    link: "../data/fr"
  - title: "Zones de peuplement et dangers naturels au Canada"
---
<link href='../assets/css/app.css' rel='stylesheet'/>

{% assign nhsl_set = site.data.nhsl.datasets | where: "id", "nhsl" %}
{% assign nhsl_text = nhsl_set[0].description[page.lang] | split: '\n' %}
{% assign para_text = nhsl_text | slice: 1, nhsl_text.size %}

<p><strong>{{ nhsl_text[0] }}</strong></p>
<div class="row">
  <div class="col-md-8">
    {% for paragraph in para_text %}
      <p>{{ paragraph | replace: "Exposition physique", "<a href='#physical_exposure'>Exposition physique</a>" | replace: "Vulnérabilité sociale", "<a href='#social_fabric'>Vulnérabilité sociale</a>" }}</p>
    {% endfor %}
    <!-- <p>La <a href='#risk_dynamics'>couche de la dynamique des risques</a> utilise l’information disponible sur la croissance de la population et les changements à l’utilisation des terres depuis 1975 pour évaluer comment l’évolution des tendances de l’urbanisation contribuent à aggraver les profils de risques naturels au fil du temps au Canada.</p> -->
    <section class="jumbotron">
      <p>Tous les produits sont publiés sous la licence du gouvernement ouvert – Canada.</p>
      <p><a href="https://ouvert.canada.ca/fr/licence-du-gouvernement-ouvert-canada" class="btn btn-info btn-lg" role="button">Voir</a></p>
    </section>
  </div>
  <div class="col-md-4">
  <div class="panel panel-primary mrgn-tp-sm">
      <div class="panel-heading">
        <div class="panel-title">Ensembles de données</div>
      </div>
      <ul class="list-group">
        <li class="list-group-item">
          <a href='#physical_exposure'>Couche de l’exposition physique</a>
        </li>
        <li class="list-group-item">
          <a href='#social_fabric'>Couche du tissu social</a>
        </li>
      </ul>
    </div>
    <div class="panel panel-primary">
      <div class="panel-heading">
        <div class="panel-title">Personne-ressource responsable de la distribution</div>
      </div>
      <ul class="list-group">
        <li class="list-group-item">
          <b>Nom de l'organisation:</b><br>
          Gouvernement du Canada;Ressources naturelles Canada;Secteur des terres et des minéraux, Commission géologique du Canada
        </li>   
        <li class="list-group-item">
          <b>Courriel:</b><br>
          <a href="mailto:GSC.info.CGC@NRCan.gc.ca">GSC.info.CGC@NRCan.gc.ca</a>
        </li>
      </ul>
    </div>
  </div>
</div>

<hr>

<a name="physical_exposure"></a>

## Exposition physique

{% assign phys_ex_set = site.data.nhsl.datasets | where: "id", "nhsl_physical_exposure_indicators" %}
{% assign phys_ex_text = phys_ex_set[0].description[page.lang] | split: '\n' %}
{% assign para_text = phys_ex_text | slice: 1, phys_ex_text.size %}

<p>
  <div class="card" style="float:left;margin:10px 20px 0px 0px;">
    <img src="../assets/img/nhsl_physical_exposure.png" width="350" class="img-rounded img-responsive"/>
    <div class="card-body">
      <a href="nhsl_physical_exposure_map.html" class="btn btn-primary btn-lg btn-block mrgn-tp-sm" role="button"> Voir sur la carte </a>
    </div>
  </div>
  <strong>{{ phys_ex_text[0] }}</strong></p>

{% for paragraph in para_text %}
  <p>{{ paragraph }}</p>
{% endfor %}

### Ressources de données

<div id="nhsl_physical_exposure_indicators">
  {% include nhsl-resources.html lang = page.lang layer = "nhsl_physical_exposure_indicators" %}
</div>

<hr>

<a name="social_fabric"></a>

## Tissu social et seuils de capacité

{% assign soc_fab_set = site.data.nhsl.datasets | where: "id", "nhsl_social_fabric_indicators" %}
{% assign soc_fab_text = soc_fab_set[0].description[page.lang] | split: '\n' %}
{% assign para_text = soc_fab_text | slice: 1, soc_fab_text.size %}

<p>
  <div class="card" style="float:left;margin:10px 20px 0px 0px;">
    <img src="../assets/img/nhsl_social_fabric.png" width="350" class="img-rounded img-responsive"/>
    <div class="card-body">
      <a href="nhsl_social_fabric_map.html" class="btn btn-primary btn-lg btn-block mrgn-tp-sm" role="button"> Voir sur la carte </a>
    </div>
  </div>
  <strong>{{ soc_fab_text[0] }}</strong></p>

{% for paragraph in para_text %}
  <p>{{ paragraph }}</p>
{% endfor %}

### Ressources de données

<div id="nhsl_social_fabric_indicators">
  {% include nhsl-resources.html lang = page.lang layer = "nhsl_social_fabric_indicators" %}
</div>

<script src="https://code.jquery.com/jquery-1.12.2.min.js"
        integrity="sha256-lZFHibXzMHo3GGeehn1hudTAP3Sc0uKXBXAzHX1sjtk=" crossorigin="anonymous"></script>

<script src="../assets/js/app.js"></script>
<script>
  showProv( [ "nhsl_physical_exposure_indicators", "nhsl_social_fabric_indicators" ] );
</script>
