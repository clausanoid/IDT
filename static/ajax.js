$( document ).ready(function() {
/* creamos una grafica de linea con informacion vacia
            var dps = [];
        /* var chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	theme: "light2",
	title:{
		text: "Distancia"
	},
	axisY:{
		includeZero: false
	},
	data: [{
		type: "line",
		dataPoints: dps
	}]
});
chart.render();

*/


    setTimeout(function()
{
    $.ajax({
        type: "GET",
        url: "http://localhost:5000/datos",
        success: function(respuesta){
          $('.center-div').html(respuesta); // vamos a escribir en el centro el valor de nuestra lectura

          // Agregamos puntos a nuestra tabla a partir de los valores que recibimos del arduino
          /* dps.push({
			y: respuesta
		}) */


    }});
}, 10000); // Haremos una solicitud cada 10 segundos


});