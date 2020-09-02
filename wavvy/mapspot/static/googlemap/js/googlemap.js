

  function initMap() {

    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 6,
      center: {lat: 37.983150, lng: 128.737988}
    });

    // Create an array of alphabetical characters used to label the markers.
    var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    var infoWin = new google.maps.InfoWindow();
    // Add some markers to the map.
    // Note: The code uses the JavaScript Array.prototype.map() method to
    // create an array of markers based on a given "locations" array.
    // The map() method here has nothing to do with the Google Maps API.
    
     //var markers = locations.map(function(location, i) {
     //  return new google.maps.Marker({
     //    position: location,
     //    label: labels[i % labels.length]
     //  });
    // });
    var markers = locations.map(function(location, i) {
      var marker =  new google.maps.Marker({
        position: location
      });
      google.maps.event.addListener(marker, 'click', function(evt) {
        infoWin.setContent(location.info);
        infoWin.open(map, marker);
      })
      return marker;
     });

    // Add a marker clusterer to manage the markers.
    var markerCluster = new MarkerClusterer(map, markers,
        {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
  }

  var locations = [
    {lat:  37.911229, lng: 128.819832, info: "<div><a href=/analysis/weather/>주문진해변</a></div>"}, //주문진해변
    {lat:  37.946317, lng: 128.783135, info: "<div><a href=/analysis/weather/>남애3리 파도보기</a></div>"}, //남애3리
    {lat:  37.949179, lng: 128.778628, info: "갯마을해변"}, //갯마을
    {lat:  37.969323, lng: 128.762804, info: "<div><a href=/analysis/weather/>인구해변</a></div>"}, //인구 
    {lat:  37.974247, lng: 128.759916, info: "<div><a href=/analysis/weather/>죽도</a></div>"}, //죽도
    {lat:  38.005810, lng: 128.731488, info: "<div><a href=/analysis/weather/>기사문</a></div>"}, //기사문
    {lat:  38.023050, lng: 128.725772, info: "<div><a href=/analysis/weather/>하조대</a></div>"}, //하조대 
    {lat:  38.130247, lng: 128.623056, info: "<div><a href=/analysis/weather/>설악</a></div>"}, //설악
    {lat:  38.153301, lng: 128.608293, info: "<div><a href=/analysis/weather/>물치</a></div>"}, //물치 
    {lat:  38.332480, lng: 128.527592, info: "<div><a href=/analysis/weather/>송지호</a></div>"}, //송지호
    {lat:  38.308704, lng: 128.542672, info: "<div><a href=/analysis/weather/>자작도</a></div>"}, //자작도
    {lat: -37.765015, lng: 145.133858},
    {lat: -37.770104, lng: 145.143299},
    {lat: -37.773700, lng: 145.145187},
    {lat: -37.774785, lng: 145.137978},
    {lat: -37.819616, lng: 144.968119},
    {lat: -38.330766, lng: 144.695692},
    {lat: -39.927193, lng: 175.053218},
    {lat: -41.330162, lng: 174.865694},
    {lat: -42.734358, lng: 147.439506},
    {lat: -42.734358, lng: 147.501315},
    {lat: -42.735258, lng: 147.438000},
    {lat: -43.999792, lng: 170.463352}
  ]

  