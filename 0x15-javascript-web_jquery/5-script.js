#!/usr/bin/node
/*
 * jQuery to append an li tag to a ul
 */

var $list = $('ul.my_list');
var $button = $('div#add_item');


$button.on('click', function () {
	$list.append('<li>Item</li>');
});
