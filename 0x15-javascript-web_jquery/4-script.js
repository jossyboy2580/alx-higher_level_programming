#!/usr/bin/node
/*
 * using jquery to toggle class
 */

var $header = $('header');
var $toggler = $('div#toggle_header');

$toggler.on('click', function () {
	if ($header.hasClass('red')) {
		$header.removeClass('red');
		$header.addClass('green');
	} else {
		$header.removeClass('green');
		$header.addClass('red');
	}
});
