#!/usr/bin/node
const request = require('request');

const sw = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(sw, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
