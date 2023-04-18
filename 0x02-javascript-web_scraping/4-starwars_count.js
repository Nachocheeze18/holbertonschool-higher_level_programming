#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const grab = JSON.parse(body).results;
    let i = 0;
    for (const title in grab) {
      const charList = grab[title].characters;
      for (const person in charList) {
        if (charList[person].includes('/18/')) {
          i++;
        }
      }
    }
    console.log(i);
  }
});
