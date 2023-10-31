let config = {
    minZoom: 7,
    maxZoom: 18,
};
// magnification with which the map will start
const zoom = 17;
// co-ordinates
const lat = 21.02528315;
const lng = 105.84213800949607;
  
  // calling map
const map = L.map("map", config).setView([lat, lng], zoom);
  
// Used to load and display tile layers on the map
// Most tile servers require attribution, which you can set under `Layer`
L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

var points = [
  [21.0210536, 105.8409287],
  [21.0228612, 105.8409566],
  [21.0228621, 105.8410001],
  [21.0231261, 105.8410075],
  [21.02333, 105.8410133],
  [21.0233319, 105.8412059],
  [21.0247813, 105.8412317],
  [21.0247821, 105.841053],
  [21.025861, 105.8410245],
  [21.0259372, 105.8410212],
  [21.0264208, 105.8410002],
  [21.0268439, 105.8410075],
  [21.0272135, 105.8410482],
  [21.027382, 105.8410999],
  [21.0273726, 105.8412423],
  [21.0274843, 105.8412544],
  [21.0276184, 105.8415184],
  [21.0286675, 105.8415658],
  [21.0287977, 105.8415583],
  [21.0286572, 105.8421285],
  [21.0293312, 105.8430539],
  [21.0275833, 105.8444973],
  [21.0274862, 105.8450064],
  [21.0271769, 105.8451781],
  [21.0267642, 105.8453741],
  [21.0266721, 105.845688],
  [21.0264024, 105.8456107],
  [21.0265691, 105.8450401],
  [21.0264424, 105.8446985],
  [21.0263056, 105.8447354],
  [21.0260314, 105.8439594],
  [21.0257842, 105.8440946],
  [21.0259032, 105.8434431],
  [21.0246276, 105.8430176],
  [21.0243061, 105.8442223],
  [21.0240062, 105.8441246],
  [21.0239629, 105.8442832],
  [21.0237428, 105.8442489],
  [21.0236472, 105.8442364],
  [21.0233458, 105.8441836],
  [21.0234688, 105.8437514],
  [21.0223668, 105.8433866],
  [21.0207155, 105.8428001],
  [21.021032, 105.8417808],
  [21.0212625, 105.8418589],
  [21.021271, 105.8411301],
  [21.0210586, 105.8411255],
  [21.0210536, 105.8409287]
];

L.polyline(points, {
    color: "red",
    weight: 3,
  })
.bindPopup("polygon")
.addTo(map);

let markers = []
var polyline

function onMapClick(e) {
  const customPopup = `Lat: ${e.latlng.lat.toFixed(4)} <br /> Lng: ${e.latlng.lng.toFixed(4)}`;
  let marker = L.marker(e.latlng).bindPopup(customPopup).addTo(map)
  marker.on("dblclick", function(){
    map.removeLayer(marker)
    markers = markers.filter(item => item != marker)
  })
  markers.push(marker)
}

map.on('click', onMapClick);

$("#btn_clear").on("click", function(){
  for(var i = 0; i < markers.length; i++){
    map.removeLayer(markers[i]);
  }
  markers = []
  map.removeLayer(polyline);
})

$('#btn_api').on("click", function() {
  console.log(markers)
  $.get("http://127.0.0.1:5000", {m1_lat: markers[0]._latlng.lat, m1_lng : markers[0]._latlng.lng, m2_lat: markers[1]._latlng.lat, m2_lng : markers[1]._latlng.lng})
  .done(function(data){
    polyline = L.polyline(data, {color: 'red'}).addTo(map);
  })
})