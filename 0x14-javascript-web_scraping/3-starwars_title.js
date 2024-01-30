#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const jsonBody = JSON.parse(body);
    console.log(jsonBody.title);
  } else console.log(response.statusCode);
});
