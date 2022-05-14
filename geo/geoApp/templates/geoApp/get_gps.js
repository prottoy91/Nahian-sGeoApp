var URL = "{% url 'get_gps' %}";
var data = {'lat': lat};
    $.post(URL, data, function(response){
        if(response === 'success'){ alert('Yay!'); }
        else{ alert('Error! :('); }
    });

-------------------------
<div class="getLocation()"></div>
, function(response){
        if(response === 'success'){ alert('Yay!'); }
        else{ alert('Error! :('); }
        }
-----------------------
function showPosition(position) {
  lat = position.coords.latitude; 
  lng = position.coords.longitude;
    x.innerHTML = "Latitude: " + lat + 
  "<br>Longitude: " + lng;
}
----------------------------
$(document).ready(function(){
		function showPosition(position) {
    	lat = position.coords.latitude; 
  		lng = position.coords.longitude;
  		x.innerHTML = "Latitude: " + lat + 
  		"<br>Longitude: " + lng;
        updateGPS();}
    });

-------------------------
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else { 
    x.innerHTML = "Geolocation is not supported by this browser.";
  }


function showPosition(position) {
  lat = position.coords.latitude; 
  lng = position.coords.longitude;
    x.innerHTML = "Latitude: " + lat + 
  "<br>Longitude: " + lng;
}

---------------------
, function(response){
        if(response === 'success'){ alert('Yay!'); }
        else if (response === 'FAIL!')  { alert('Error! :('); }
        }); 
        
        --------------------
        
$(document).ready(function(){
		if (navigator.geolocation) {
    		navigator.geolocation.getCurrentPosition(showPosition);
  		} 
  		else 
  		{ 
    		x.innerHTML = "Geolocation is not supported by this browser.";
  		}
		function showPosition(position) {
    	lat = position.coords.latitude; 
  		lng = position.coords.longitude;
  		x.innerHTML = "Latitude: " + lat + 
  		"<br>Longitude: " + lng;
        updateGPS();}
    });
-----------------------------------------
    function updateGPS(){

var data = {'lat':lat, csrfmiddlewaretoken: '{{ csrf_token }}'};
    $.post(URL, data, function(){
         alert('Yay!'); 
    })
    .done(function() {
    alert( "second success" );
  })
  .fail(function() {
    alert( "error" );
  })
  .always(function() {
    alert( "finished" );
  }); 
}
-----------------------------------------
$.post(URL, data, function(){
      alert('Yay!');    
    })

-----------------------------------------
if (navigator.geolocation) {
    		navigator.geolocation.getCurrentPosition(showPosition);
  		} 
  		else 
  		{ 
    		x.innerHTML = "Geolocation is not supported by this browser.";
  		}
		function showPosition(position) {
    	lat = position.coords.latitude; 
  		lng = position.coords.longitude;
  		x.innerHTML = "Latitude: " + lat + 
  		"<br>Longitude: " + lng;
  		}
