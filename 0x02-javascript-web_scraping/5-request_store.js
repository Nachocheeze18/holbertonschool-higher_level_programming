#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.appendFile(process.argv[3], body, function (appendError) {
      if (appendError) {
        console.log(appendError);
      }
    });
  }
});
