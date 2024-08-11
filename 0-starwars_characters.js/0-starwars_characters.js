#!/usr/bin/node

const request = require('request');
const number = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${number}`;

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const chars = JSON.parse(body).characters;
    const names = [];

    let requestsCompleted = 0;

    for (const c of chars) {
      request(c, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          names.push(JSON.parse(body).name);
        }
        requestsCompleted++;

        if (requestsCompleted === chars.length) {
          names.forEach(name => console.log(name));
        }
      });
    }
  }
});
