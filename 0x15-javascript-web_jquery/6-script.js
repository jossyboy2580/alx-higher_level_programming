#!/usr/bin/node
/*
 * jquery to change the text content of the header
 */

var $header = $('header');
var $button = $('div#update_header');

$button.on('click', function () {
	$header.text('New Header!!!');
});
