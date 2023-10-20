mapboxgl.accessToken = 'pk.eyJ1Ijoic2FtYmF5b3lvIiwiYSI6ImNsbnV5NXMybzA0Z28ycW15bDV0cGExdGwifQ.RoFdT8Nr0KzFofOK-h-5mA'

let map = new mapboxgl.Map({
	container: 'map',
	style: 'mapbox://styles/mapbox/streets-v10',
	center: [-74.806984, 10.988997],
	zoom: 13
});



// Lista para almacenar los marcadores
var markers = [];

// Función para añadir un marcador al mapa
function addMarker(longitude, latitude) {
    var marker = new mapboxgl.Marker().setLngLat([longitude, latitude]).addTo(map);
    markers.push(marker);
    return marker;
}

// Función para eliminar todos los marcadores del mapa
function removeAllMarkers() {
    markers.forEach(function(marker) {
        marker.remove();
    });
    markers = [];
    // Elimina la ruta del mapa
    map.removeLayer('route');
    map.removeSource('route');
}

// Función para trazar una ruta entre dos marcadores
function traceRoute(startPoint, endPoint) {
    // Utiliza la API de direcciones de Mapbox para trazar la ruta
    var directionsRequest = 'https://api.mapbox.com/directions/v5/mapbox/driving/' +
        startPoint.lng + ',' + startPoint.lat + ';' +
        endPoint.lng + ',' + endPoint.lat +
        '?steps=true&geometries=geojson&access_token=' + mapboxgl.accessToken;

    fetch(directionsRequest)
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            var route = data.routes[0].geometry;
            // Añade la ruta al mapa
            map.addLayer({
                id: 'route',
                type: 'line',
                source: {
                    type: 'geojson',
                    data: {
                        type: 'Feature',
                        geometry: route
                    }
                },
                paint: {
                    'line-width': 5,
                    'line-color': '#007cbb'
                }
            });
        });
}

// Evento al hacer clic en el mapa para añadir un marcador
map.on('click', function (e) {
    if (markers.length < 2) { // Limita la cantidad de marcadores a 2
      var longitude = e.lngLat.lng;
      var latitude = e.lngLat.lat;
      alert('longitud: ' + longitude + ' latitud: ' + latitude)
      var marker = addMarker(longitude, latitude);
      markers.push(marker);
  
      // Si hay al menos dos marcadores, traza la ruta
      if (markers.length === 2) {
        traceRoute(markers[0].getLngLat(), markers[1].getLngLat());
      }
    }
  });
  
  function addMarker(longitude, latitude) {
    var marker = new mapboxgl.Marker().setLngLat([longitude, latitude]).addTo(map);
    return marker;
  }



// Evento para eliminar todos los marcadores
document.getElementById('add-marker').addEventListener('click', function() {
    removeAllMarkers();
});

// Evento para eliminar todos los marcadores
document.getElementById('remove-markers').addEventListener('click', function() {
    removeAllMarkers();
});




