---
authorName: Natural Resources Canada
authorUrl:
dateModified: 2025-01-21
pageclass: wb-prettify all-pre
subject:
  en: [GV Government and Politics, Government services]
  fr: [GV Gouvernement et vie politique, Services gouvernementaux]
title: Zones de peuplement et dangers naturels au Canada
lang: fr
altLangPage: ../en/
nositesearch: true
nomenu: true
nofooter: true
breadcrumbs:
  - title: "OpenDRR"
    link: "https://www.github.com/OpenDRR/"
  - title: "Téléchargements de OpenDRR"
    link: "../downloads/fr/"
  - title: "Zones de peuplement et dangers naturels au Canada"
---
<link href='../assets/css/app.css' rel='stylesheet'/>

{% assign nhsl_text = site.data.nhsl.description[page.lang] | split: '\n' %}
{% assign para_text = nhsl_text | slice: 1, nhsl_text.size %}

<p><strong>{{ nhsl_text[0] }}</strong></p>
<div class="row">
  <div class="col-md-8">
    {% for paragraph in para_text %}
      <p>{{ paragraph | replace: "Exposition physique", "<a href='#nhsl_physical_exposure_indicators-a'>Exposition physique</a>" | replace: "Vulnérabilité sociale", "<a href='#nhsl_social_fabric_indicators-a'>Vulnérabilité sociale</a>" }}</p>
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
        {% for layer in site.data.nhsl.layers %}
        <li class="list-group-item">
          {% assign text = site.data.nhsl.datasets | where: "id", layer %}
          <a href='#{{ layer }}-a'>{{ text[0].title[page.lang] }}</a>
        </li>
        {% endfor %}
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

{% assign variables = "'" %}
{% for layer in site.data.nhsl.layers %}

  {% assign variables = variables | append: layer | append: "', '" %}
  {% assign layer_set = site.data.nhsl.datasets | where: "id", layer %}
  {% assign layer_text = layer_set[0].description[page.lang] | split: '\n' %}
  {% assign para_text = layer_text | slice: 1, layer_text.size %}

  <hr>

  <a name="{{ layer }}-a"></a>

  <h2>{{ layer_set[0].title[page.lang] }}</h2>

  <p>
    <div class="card" style="float:left;margin:10px 20px 0px 0px;">
      <img src="../assets/img/{{ layer }}.png" width="350" class="img-rounded img-responsive"/>
      <div class="card-body">
        <a href="{{ layer }}_map.html" class="btn btn-primary btn-lg btn-block mrgn-tp-sm" role="button"> Voir sur la carte </a>
      </div>
    </div>
    <strong>{{ layer_text[0] }}</strong>
  </p>

  <div>
  {% for paragraph in para_text %}
    <p>{{ paragraph }}</p>
  {% endfor %}
  </div>

  <div id={{ layer }} class="col-md-12">
    <h3>Ressources de données</h3>
    {% include nhsl-resources.html lang = page.lang layer = layer %}
  </div>

{% endfor %}

{% assign var_length = variables.size | minus: 3 %}
{% assign variables = variables | slice: 0, var_length %}

<script src="https://code.jquery.com/jquery-1.12.2.min.js"
        integrity="sha256-lZFHibXzMHo3GGeehn1hudTAP3Sc0uKXBXAzHX1sjtk=" crossorigin="anonymous"></script>

<script src="../assets/js/app.js"></script>
<script>
  let layers = [{{ variables }}];
  showProv( layers );
</script>
