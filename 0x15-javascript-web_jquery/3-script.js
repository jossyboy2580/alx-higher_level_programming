#!/usr/bin/node
/*
 * Add a class to a header
 */

var $header = $('header');
var $button = $('div#red_header');

$button.on('click', function () {
	$header.addClass('red');
})
