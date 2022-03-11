---
authorName: Natural Resources Canada
authorUrl:
dateModified: 2021-07-26
noContentTitle: true
pageclass: wb-prettify all-pre
subject:
  en: [GV Government and Politics, Government services]
  fr: [GV Gouvernement et vie politique, Services gouvernementaux]
title: Physical Exposure
lang: en
altLangPage: ../fr/nhsl_physical_exposure_indicators_map
nositesearch: true
nomenu: true
nofooter: true
breadcrumbs:
  - title: "OpenDRR"
    link: "https://www.github.com/OpenDRR/"
  - title: "OpenDRR Downloads"
    link: "../downloads/en"
  - title: "Human Settlement and Natural Hazards in Canada"
    link: "/en/"
  - title: "Physical Exposure"
    link: "/en/index#nhsl_physical_exposure_indicators-a"
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
<link href='https://api.mapbox.com/mapbox.js/plugins/leaflet-fullscreen/v1.0.1/leaflet.fullscreen.css' rel='stylesheet'/>

<script src="https://code.jquery.com/jquery-3.6.0.slim.min.js" integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>

<link href='../assets/css/app.css' rel='stylesheet'/>

<div id="map"></div>
<div id="sidebar"></div>

{% assign variables = '' %}
{% for attribute in site.data.nhsl_physical_exposure_attributes.attributes %}
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

	var natural_hazards_building_exposure_model = L.esri.featureLayer({
		url: 'https://maps-cartes.services.geo.ca/server_serveur/rest/services/NRCan/nhsl_en/MapServer/7',
		simplifyFactor: 0.25,
		precision: 5,
    minZoom: 10,
		fields: [ 'OBJECTID', 'E_BldgNum' ]
	}).on( 'load', function ( e ) {
    $( '#sidebar' ).html( '' );
		this.metadata( function ( error, metadata ) {
			buildLegend( metadata );
		});
		$( '#modal' ).remove();
	}).on( 'loading', function ( e ) {
		$( '#map' ).before( '<div id="modal"></div>' );
	}).bindPopup( function ( layer ) {
    	return L.Util.template( '<p>Number of buildings: <strong>{E_BldgNum}</strong></p>', layer.feature.properties );
  }).on('add', function ( e ) {
    if ( oldId && oldLayer ) {
		  $( '#sidebar' ).html( '' );
      oldLayer.resetFeatureStyle( oldId );
    }
  }).on('click', function ( e ) {
		showAttributes( e, natural_hazards_building_exposure_model );
  });

	var landuse = L.esri.featureLayer({
		url: 'https://maps-cartes.services.geo.ca/server_serveur/rest/services/NRCan/nhsl_en/MapServer/8',
		simplifyFactor: 0.25,
		precision: 5,
    minZoom: 10,
		fields: [ 'OBJECTID', 'E_LandUse' ]
	}).on( 'load', function ( e ) {
		this.metadata( function ( error, metadata ) {
			buildLegend( metadata );
		});
		$( '#modal' ).remove();
	}).on( 'loading', function ( e ) {
		$( '#map' ).before( '<div id="modal"></div>' );
	}).bindPopup( function ( layer ) {
    	return L.Util.template( '<p>Landuse: <strong>{E_LandUse}</strong></p>', layer.feature.properties );
  }).on('add', function ( e ) {
    if ( oldId && oldLayer) {
		  $( '#sidebar' ).html( '' );
      oldLayer.resetFeatureStyle( oldId );
    }
  }).on('click', function ( e ) {
		showAttributes( e, landuse );
  });

  var population_density = L.esri.featureLayer({
		url: 'https://maps-cartes.services.geo.ca/server_serveur/rest/services/NRCan/nhsl_en/MapServer/9',
		simplifyFactor: 0.25,
		precision: 5,
    minZoom: 10,
		fields: [ 'OBJECTID', 'Et_PopNight___E_AreaHa' ]
  }).on( 'load', function ( e ) {
		this.metadata( function ( error, metadata ) {
			buildLegend( metadata );
		});
		$( '#modal' ).remove();
	}).on( 'loading', function ( e ) {
		$( '#map' ).before( '<div id="modal"></div>' );
	}).bindPopup( function ( layer ) {
    	return L.Util.template( '<p>Population density: <strong>{Et_PopNight___E_AreaHa}</strong></p>', layer.feature.properties );
  }).on('add', function ( e ) {
    if ( oldId && oldLayer) {
		  $( '#sidebar' ).html( '' );
      oldLayer.resetFeatureStyle( oldId );
    }
  }).on('click', function ( e ) {
		showAttributes( e, population_density );
  });

  var building_assets_per_hectare = L.esri.featureLayer({
		url: 'https://maps-cartes.services.geo.ca/server_serveur/rest/services/NRCan/nhsl_en/MapServer/10',
		simplifyFactor: 0.25,
		precision: 5,
    minZoom: 10,
		fields: [ 'OBJECTID', 'Et_AssetValue___E_AreaHa' ]
  }).on( 'load', function ( e ) {
		this.metadata( function ( error, metadata ) {
			buildLegend( metadata );
		});
		$( '#modal' ).remove();
	}).on( 'loading', function ( e ) {
		$( '#map' ).before( '<div id="modal"></div>' );
	}).bindPopup( function ( layer ) {
    	var assetval =  L.Util.template( '{Et_AssetValue___E_AreaHa}', layer.feature.properties );
      return '<p>Building assets per hectare: <strong>' + formatter.format(assetval) + '</strong></p>';
  }).on('add', function ( e ) {
    if ( oldId && oldLayer) {
		  $( '#sidebar' ).html( '' );
      oldLayer.resetFeatureStyle( oldId );
    }
  }).on('click', function ( e ) {
		showAttributes( e, building_assets_per_hectare );
  });

	var building_density = L.esri.featureLayer({
		url: 'https://maps-cartes.services.geo.ca/server_serveur/rest/services/NRCan/nhsl_en/MapServer/11',
		simplifyFactor: 0.25,
		precision: 5,
    minZoom: 10,
		fields: [ 'OBJECTID', 'Et_BldgNum___E_AreaHa' ]
	}).on( 'load', function ( e ) {
		this.metadata( function ( error, metadata ) {
			buildLegend( metadata );
		});
		$( '#modal' ).remove();
	}).on( 'loading', function ( e ) {
		$( '#map' ).before( '<div id="modal"></div>' );
	}).bindPopup( function ( layer ) {
    return L.Util.template( '<p>Building density: <strong>{Et_BldgNum___E_AreaHa}</strong></p>', layer.feature.properties );
  }).on('add', function ( e ) {
    if ( oldId && oldLayer) {
		  $( '#sidebar' ).html( '' );
      oldLayer.resetFeatureStyle( oldId );
    }
  }).on('click', function ( e ) {
		showAttributes( e, building_density );
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
    'Landuse': landuse,
    'Population Density': population_density,
    'Building Assets per Hectare': building_assets_per_hectare,
    'Building Density': building_density,
    // 'Natural Hazards Building Exposure Model': natural_hazards_building_exposure_model
  };

  L.control.layers( overlays, null, { collapsed: false } ).addTo( map );

  landuse.addTo( map );

  var formatter = new Intl.NumberFormat( 'en-US', {
    style: 'currency',
    currency: 'USD',
    maximumFractionDigits: 0

    // These options are needed to round to whole numbers if that's what you want.
    //minimumFractionDigits: 0, // (this suffices for whole numbers, but will print 2500.10 as $2,500.1)
    //maximumFractionDigits: 0, // (causes 2500.99 to be printed as $2,501)
    //Usage: formatter.format(2500); $2,500.00
  });

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
            detail = window[key + 'Detail'];
            format = window[key + 'Format'];
            value = props[key];

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
              '<td class="attr"><span class="prop" title="' + detail + '">' + desc + '</span><span class="val">' + value + '</span></td>';
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
