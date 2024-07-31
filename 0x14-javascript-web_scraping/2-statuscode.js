#!/usr/bin/node
/**
 * perform a get request and print the status code
 */

const request = require('request');

const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
