---
authorName: Natural Resources Canada
authorUrl:
dateModified: 2021-07-26
noContentTitle: true
pageclass: wb-prettify all-pre
subject:
  en: [GV Government and Politics, Government services]
  fr: [GV Gouvernement et vie politique, Services gouvernementaux]
title: Social Vulnerability
lang: en
altLangPage: ../fr/nhsl_social_fabric_indicators_map
nositesearch: true
nomenu: true
nofooter: true
breadcrumbs:
  - title: "OpenDRR"
    link: "https://www.github.com/OpenDRR/"
  - title: "OpenDRR Downloads"
    link: "../data/en"
  - title: "Human Settlement and Natural Hazards in Canada"
    link: "/en/"
  - title: "Social Vulnerability"
    link: "/en/index#nhsl_social_fabric_indicators-a"
---
<!-- Load Leaflet from CDN -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"
integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A=="
crossorigin=""/>

<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"
integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA=="
crossorigin=""></script>

<!-- Load Esri Leaflet from CDN -->
<script src="https://unpkg.com/esri-leaflet@3.0.2/dist/esri-leaflet.js"
integrity="sha512-myckXhaJsP7Q7MZva03Tfme/MSF5a6HC2xryjAM4FxPLHGqlh5VALCbywHnzs2uPoF/4G/QVXyYDDSkp5nPfig=="
crossorigin=""></script>

<!-- Load Esri Leaflet Renderers plugin to use feature service symbology -->
<script src="https://unpkg.com/esri-leaflet-renderers@2.1.2" crossorigin=""></script>

<script src='https://api.mapbox.com/mapbox.js/plugins/leaflet-fullscreen/v1.0.1/Leaflet.fullscreen.min.js'></script>
<link href='https://api.mapbox.com/mapbox.js/plugins/leaflet-fullscreen/v1.0.1/leaflet.fullscreen.css' rel='stylesheet' />

<script src="https://code.jquery.com/jquery-3.6.0.slim.min.js" integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>

<link href='../assets/css/app.css' rel='stylesheet'/>

<div id="map"></div>
<div id="sidebar"></div>

{% assign variables = '' %}
{% for attribute in site.data.nhsl_social_fabric_attributes.attributes %}
  {% capture variable %}
  window['{{attribute.name}}' + 'Desc'] = '{{attribute.description[page.lang]}}';
  window['{{attribute.name}}' + 'Detail'] = '{{attribute.detailed[page.lang]}}';
  window['{{attribute.name}}' + 'Format'] = Number('{{attribute.format}}');
  {% endcapture %}
  {% assign variables = variables | append: variable %}
{% endfor %}

<script>

	{{variables}}

	var tiles = L.tileLayer( '//{s}.tile.osm.org/{z}/{x}/{y}.png', {
		attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
	});

	var total_social_vulnerability_score = L.esri.featureLayer({
		url: 'https://maps-cartes.services.geo.ca/server_serveur/rest/services/NRCan/nhsl_en/MapServer/1',
		simplifyFactor: 0.25,
		precision: 5,
    minZoom: 10,
		fields: [ 'OBJECTID', 'SVlt_Score' ]
	}).on( 'load', function ( e ) {
		this.metadata( function ( error, metadata ) {
			buildLegend( metadata );
		});
		$( '#modal' ).remove();
	}).on( 'loading', function ( e ) {
		$( '#map' ).before( '<div id="modal"></div>' );
	}).bindPopup( function ( layer ) {
    	return L.Util.template( '<p>Social vulnerabilty score: <strong>{SVlt_Score}</strong></p>', layer.feature.properties );
	}).on('add', function ( e ) {
    	if ( oldId && oldLayer) {
		  $( '#sidebar' ).html( '' );
      	  oldLayer.resetFeatureStyle( oldId );
    	}
  	}).on('click', function ( e ) {
		showAttributes( e, total_social_vulnerability_score );
  	});

	var financial_agency_score = L.esri.featureLayer({
		url: 'https://maps-cartes.services.geo.ca/server_serveur/rest/services/NRCan/nhsl_en/MapServer/2',
		simplifyFactor: 0.25,
		precision: 5,
    minZoom: 10,
		fields: [ 'OBJECTID', 'VEt_Score' ]
	}).on( 'load', function ( e ) {
		this.metadata( function ( error, metadata ) {
			buildLegend( metadata );
		});
		$( '#modal' ).remove();
	}).on( 'loading', function ( e ) {
		$( '#map' ).before( '<div id="modal"></div>' );
	}).bindPopup( function ( layer ) {
    	return L.Util.template( '<p>Financial agency score: <strong>{VEt_Score}</strong></p>', layer.feature.properties );
	}).on('add', function ( e ) {
    	if ( oldId && oldLayer) {
		  $( '#sidebar' ).html( '' );
      	  oldLayer.resetFeatureStyle( oldId );
    	}
  	}).on('click', function ( e ) {
		showAttributes( e, financial_agency_score );
  	});

    var housing_condition_score = L.esri.featureLayer({
		url: 'https://maps-cartes.services.geo.ca/server_serveur/rest/services/NRCan/nhsl_en/MapServer/3',
		simplifyFactor: 0.25,
		precision: 5,
    minZoom: 10,
		fields: [ 'OBJECTID', 'VHt_Score' ]
  	}).on( 'load', function ( e ) {
		this.metadata( function ( error, metadata ) {
			buildLegend( metadata );
		});
		$( '#modal' ).remove();
	}).on( 'loading', function ( e ) {
		$( '#map' ).before( '<div id="modal"></div>' );
	}).bindPopup( function ( layer ) {
    	return L.Util.template( '<p>Housing condition score: <strong>{VHt_Score}</strong></p>', layer.feature.properties );
	}).on('add', function ( e ) {
    	if ( oldId && oldLayer) {
		  $( '#sidebar' ).html( '' );
      	  oldLayer.resetFeatureStyle( oldId );
    	}
  	}).on('click', function ( e ) {
		showAttributes( e, housing_condition_score );
  	});

    var social_connectivity_score = L.esri.featureLayer({
		url: 'https://maps-cartes.services.geo.ca/server_serveur/rest/services/NRCan/nhsl_en/MapServer/4',
		simplifyFactor: 0.25,
		precision: 5,
    minZoom: 10,
		fields: [ 'OBJECTID', 'VFt_Score' ]
  	}).on( 'load', function ( e ) {
		this.metadata( function ( error, metadata ) {
			buildLegend( metadata );
		});
		$( '#modal' ).remove();
	}).on( 'loading', function ( e ) {
		$( '#map' ).before( '<div id="modal"></div>' );
	}).bindPopup( function ( layer ) {
    	return L.Util.template( '<p>Social connectivity score: <strong>{VFt_Score}</strong></p>', layer.feature.properties );
	}).on('add', function ( e ) {
    	if ( oldId && oldLayer) {
		  $( '#sidebar' ).html( '' );
      	  oldLayer.resetFeatureStyle( oldId );
    	}
  	}).on('click', function ( e ) {
		showAttributes( e, social_connectivity_score );
  	});

	var individual_autonomy_score = L.esri.featureLayer({
		url: 'https://maps-cartes.services.geo.ca/server_serveur/rest/services/NRCan/nhsl_en/MapServer/5',
		simplifyFactor: 0.25,
		precision: 5,
    minZoom: 10,
		fields: [ 'OBJECTID', 'VAt_Score' ]
	}).on( 'load', function ( e ) {
		this.metadata( function ( error, metadata ) {
			buildLegend( metadata );
		});
		$( '#modal' ).remove();
	}).on( 'loading', function ( e ) {
		$( '#map' ).before( '<div id="modal"></div>' );
	}).bindPopup( function ( layer ) {
    	return L.Util.template( '<p>Individual autonomy score: <strong>{VAt_Score}</strong></p>', layer.feature.properties );
	}).on('add', function ( e ) {
    	if ( oldId && oldLayer) {
		  $( '#sidebar' ).html( '' );
      	  oldLayer.resetFeatureStyle( oldId );
    	}
  	}).on('click', function ( e ) {
		showAttributes( e, individual_autonomy_score );
  	});

  var map = L.map( 'map', {
    fullscreenControl: true,
    center: [ 49.2827, -123.1207 ],
    zoom: 12,
    layers: [ tiles ]
  }),
  legend = L.control( { position: 'bottomright' } );

  map.on( 'overlayadd', function() {
    $( '#map' ).before( '<div id="modal"></div>' );
  });

  map.on( 'fullscreenchange', function () {
    map.invalidateSize();
  });

  var overlays = {
    'Total Social Vulnerability Score': total_social_vulnerability_score,
    'Financial Agency Score': financial_agency_score,
    'Housing Condition Score': housing_condition_score,
    'Social Connectivity Score': social_connectivity_score,
    'Individual Autonomy Score': individual_autonomy_score
  };

  L.control.layers( overlays, null, { collapsed: false } ).addTo( map );

  total_social_vulnerability_score.addTo( map );

  var oldId;
  var oldLayer;  

  function showAttributes( e, current_layer ) {

    current_layer.resetFeatureStyle( oldId );

    oldId = e.layer.feature.id;
    oldLayer = current_layer;

    current_layer.setFeatureStyle(e.layer.feature.id, {
      fillColor: 'red',
      color: 'red',
      weight: 3,
      fillOpacity: 0.5
    });
      
    current_layer.query()
      .where("OBJECTID = " + e.layer.feature.id )
      .run( function( error, resp ) {

        let props = resp.features[0].properties,
          string = '<table class="table table-striped table-responsive"><tr>';

          counter = 1;
          for ( const key in props ) {

            desc = window[key + 'Desc'];
            detail = window[key + 'Detail']
            format = window[key + 'Format']
            value = props[key]

            if ( format && value ) {
              if ( format === 444 ) {
                value = value.toLocaleString(undefined, {style:'currency', currency:'USD'});
              }
			  else if ( format === 111 ) {
                value = value.toLocaleString(undefined, { maximumFractionDigits: 0 })
              }
			  else if ( format === 555 ) {
                value *= 100
                value = value.toLocaleString(undefined, { maximumFractionDigits: 2 });
                value += '%';
              }
              else if ( format < 0 ) {
                mult = Math.abs(format);
                rounded = Math.round(value / (10 ** mult)) * 10 ** mult;
                value = rounded.toLocaleString(undefined);
              }
              else if ( format > 0 ) {
                value = value.toLocaleString(undefined, { maximumFractionDigits: format });
              }

              string +=
              '<td class="attr"><span class="prop" title="' + detail + '">' + desc + ' - ' + key + '</span><span class="val">' + value + '</span></td>';
            }
            else if ( key === 'OBJECTID' || key === 'SHAPE_Length' || key === 'SHAPE_Area' ) {}
			else if ( desc ) {
              string +=
                '<td class="attr"><span class="prop" title="' + detail + '">' + desc + '</span><span class="val">' + value + '</span></td>';
            }
            else {
              string +=
              '<td class="attr"><span class="prop">' + key + '</span><span class="val">' + value + '</span></td>';
            }
            if ( counter % 3 === 0) {
                string += '</tr><tr>';
              }
            counter += 1;
          }
        string += '</tr></table>';
        $( '#sidebar' ).html( '<h3>Properties of Selected Feature</h3>' + string );

      });
  }

  function buildLegend( metadata ) {

	map.removeControl(legend);
	
	var renderers = metadata.drawingInfo.renderer.classBreakInfos ? metadata.drawingInfo.renderer.classBreakInfos : metadata.drawingInfo.renderer.uniqueValueInfos;

	legend.onAdd = function ( map ) {

		var div = L.DomUtil.create( 'div', 'info legend' );

		if ( renderers.length === 0 ) { 
			return L.DomUtil.create( 'div' ); 
		}

		div.innerHTML += '<center><strong>' + metadata.name + '</strong></center>';

		for ( var i = 0; i < renderers.length; i++ ) {
			div.innerHTML +=
			'<div style="white-space: nowrap;margin-top: 2px;"><i style="background:rgb( ' + renderers[i][ 'symbol' ].color[0] + ',' + renderers[i][ 'symbol' ].color[1] + ',' + renderers[i][ 'symbol' ].color[2] + ',' + renderers[i][ 'symbol' ].color[3] + ' );border-color:rgb( ' + renderers[i][ 'symbol' ][ 'outline' ].color[0] + ',' + renderers[i][ 'symbol' ][ 'outline' ].color[1] + ',' + renderers[i][ 'symbol' ][ 'outline' ].color[2]+ ',' + renderers[i][ 'symbol' ][ 'outline' ].color[3] + ' );border-width:' + renderers[i][ 'symbol' ][ 'outline' ].width + 'px;"></i> ' +
			renderers[i][ 'label' ] + '</div>';
		}

		return div;

	};

    legend.addTo( map );
  }
</script>
