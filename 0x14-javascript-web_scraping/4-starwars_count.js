#!/usr/bin/node
/* STAR WARS CHARACTER 18 Wedge Antilles */

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const jsonBody = JSON.parse(body);
    console.log(jsonBody.results.filter(item => {
      return item.characters.some(url => url.includes('/18/'));
    }).length);
  } else {
    console.log(response.statusCode);
  }
});
