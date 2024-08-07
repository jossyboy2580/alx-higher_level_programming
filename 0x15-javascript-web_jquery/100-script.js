#!/usr/bin/node
/*
 * Using jquery to fetch data from an API
 */

var $movie_container = $('ul#list_movies');


$.ajax({
	type: "GET",
	url: "https://swapi-api.alx-tools.com/api/films/?format=json",
	success: function (data) {
		var $results = data.results;
		$.each($results, function (index, value) {
			$movie_container.append("<li>" + value.title +"</li>");
		});
	},
	error: function () {
		console.log('error');
	}
});
