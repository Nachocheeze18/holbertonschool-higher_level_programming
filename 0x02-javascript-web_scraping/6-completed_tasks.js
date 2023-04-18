#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const completedTasks = {};
    const data = JSON.parse(body);
    for (let i = 0; i < data.length; i++) {
      const userId = data[i].userId;
      const complete = data[i].completed;
      if (complete) {
        if (!completedTasks[userId]) {
          completedTasks[data[i].userId] = 1;
        } else {
          completedTasks[data[i].userId] += 1;
        }
      }
    }
    console.log(completedTasks);
  }
});
