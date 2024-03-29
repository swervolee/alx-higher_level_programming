#!/usr/bin/node
/* TASKS COMPLETED OBJECT */

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const jsonBody = JSON.parse(body);
    const answer = {};

    for (const x in jsonBody) {
      if (jsonBody[x].completed) {
        const id = `${jsonBody[x].userId}`;

        if (answer[id]) {
          answer[id]++;
        } else {
          answer[id] = 1;
        }
      }
    }
    console.log(answer);
  } else {
    console.log(response.statusCode);
  }
});
