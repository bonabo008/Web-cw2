var directionsDisplay;
var directionsService = new google.maps.DirectionsService();
var map;

// Initializing the map
function initialize() {
	
	directionsDisplay = new google.maps.DirectionsRenderer();
  	var farmHouse = new google.maps.LatLng(52.313365, 1.659623);
	
	//Googel map settings
	var mapOptions = {
		center: farmHouse,
		zoom: 15,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	}

	map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
  	directionsDisplay.setMap(map);

	// HTML for house info window
	var houseInfo = '<div id="content">'+
	  '<div id="siteNotice">'+
	  '</div>'+
	  '<h3 id="firstHeading">Old Farm</h3>'+
	  '</div>';
	  
	// House marker info window
	var infoWindow = new google.maps.InfoWindow({
		content: houseInfo
	});
	
	//house marker
	var marker = new google.maps.Marker({
		position: map.getCenter(),
		map: map,
		title: 'Apartment'
	});

	//go to house when marker is clicked
	google.maps.event.addListener(marker, 'click', function() {
		map.setZoom(15);
		map.setCenter(marker.getPosition());
		infoWindow.open(map,marker);
	});
	
	// end of initialize()
	}

// Google map Directions
function calcRoute() {
  var start = document.getElementById("start").value;
  var end = document.getElementById("end").value;
  var request = {
    origin:start,
    destination:end,
    travelMode: google.maps.TravelMode.DRIVING
  };
  directionsService.route(request, function(result, status) {
    if (status == google.maps.DirectionsStatus.OK) {
		directionsDisplay.setDirections(result);
		document.getElementById("start").value = "";
    }
	 else{
		  alert("Address invalid");
	  }
  });
}

// Start initialize function on load
google.maps.event.addDomListener(window, 'load', initialize);
