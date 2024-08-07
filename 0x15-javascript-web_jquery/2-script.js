#!/usr/bin/node
/*
 * jQuery code to change the color of a text
 */

var $header = $('header');
var $button = $('div#red_header');

$button.on('click', function () {
	$header.css('color', '#FF0000');
});
