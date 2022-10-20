---
authorName: Natural Resources Canada
authorUrl:
dateModified: 2022-10-19
pageclass: wb-prettify all-pre
subject:
  en: [GV Government and Politics, Government services]
  fr: [GV Gouvernement et vie politique, Services gouvernementaux]
title: Human Settlement and Natural Hazards in Canada
lang: en
altLangPage: ../fr
nositesearch: true
nomenu: true
nofooter: true
breadcrumbs:
  - title: "OpenDRR"
    link: "https://www.github.com/OpenDRR/"
  - title: "OpenDRR Downloads"
    link: "../downloads/en"
  - title: "Human Settlement and Natural Hazards in Canada"
---
<link href='../assets/css/app.css' rel='stylesheet'/>

{% assign nhsl_text = site.data.nhsl.description[page.lang] | split: '\n' %}
{% assign para_text = nhsl_text | slice: 1, nhsl_text.size %}

<p><strong>{{ nhsl_text[0] }}</strong></p>
<div class="row">
  <div class="col-md-8">
    {% for paragraph in para_text %}
      <p>{{ paragraph | replace: "Physical Exposure Layer", "<a href='#nhsl_physical_exposure_indicators-a'>Physical Exposure Layer</a>" | replace: "Social Vulnerability", "<a href='#nhsl_social_fabric_indicators-a'>Social Vulnerability</a>" }}</p>
    {% endfor %}
    <!-- <p style="text-align:justify;">The <a href='#nhsl_hazard_threat_indicators-a'>Risk Dynamics Layer</a> utilizes information on population growth and land use change since 1975 to evaluate how evolving patterns of urbanization are contributing to escalating profiles of natural risk over time across Canada.</p> -->
    <section class="jumbotron">
      <p>All products are released under the Open Government Licence - Canada.</p>
      <p><a href="https://open.canada.ca/en/open-government-licence-canada" class="btn btn-info btn-lg" role="button">Learn more</a></p>
    </section>
  </div>
  <div class="col-md-4">
    <div class="panel panel-primary mrgn-tp-sm">
      <div class="panel-heading">
        <div class="panel-title">Datasets</div>
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
        <div class="panel-title">Distribution contact</div>
      </div>
      <ul class="list-group">
        <li class="list-group-item">
          <b>Organization name:</b><br>
          Government of Canada;Natural Resources Canada;Lands and Minerals Sector, Geological Survey of Canada
        </li>
        <li class="list-group-item">
          <b>Email:</b><br>
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
        <a href="{{ layer }}_map.html" class="btn btn-primary btn-lg btn-block mrgn-tp-sm" role="button"> View on Map </a>
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
    <h3>Data Resources</h3>
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
