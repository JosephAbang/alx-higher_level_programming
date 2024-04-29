#!/usr/bin/node

const req = require('request');
const link = process.argv[2];

req(link, function (error, response, content) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const finishedTasks = {};
    const tasksData = JSON.parse(content);
    for (const index in tasksData) {
      const taskItem = tasksData[index];
      if (taskItem.completed === true) {
        if (finishedTasks[taskItem.userId] === undefined) {
          finishedTasks[taskItem.userId] = 1;
        } else {
          finishedTasks[taskItem.userId]++;
        }
      }
    }
    console.log(finishedTasks);
  } else {
    console.log('An error occurred. Status code: ' + response.statusCode);
  }
});
