#!/usr/bin/node
/*
 * Using jquery to fetch data from an API
 */

var $name_location = $('div#character');


$.ajax({
	type: "GET",
	url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
	success: function (data) {
		$name_location.text(data.name);
	},
	error: function () {
		console.log('error');
	},
});
