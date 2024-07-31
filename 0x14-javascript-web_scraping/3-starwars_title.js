#!/usr/bin/node
/**
 * A module that fetches star wars title
 */

const request = require('request');

const movieId = process.argv[2];
const endPoint = 'https://swapi-api.alx-tools.com/api/films/';

request(endPoint + movieId, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
