#!/usr/bin/node
/**
 * A script that prints the number of movies
 * 'Wedge Antiles' starred in
 */

const request = require('request');

const endPoint = 'https://swapi-api.alx-tools.com/api/films/';

const targetUrl = 'https://swapi-api.alx-tools.com/api/people/18';

request(endPoint, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    data = JSON.parse(body);
    let count = 0;
    iter = data.results;
    for (const item of iter) {
      if (targetUrl in item.characters) {
        count++;
      }
    }
    console.log(count);
  }
});
