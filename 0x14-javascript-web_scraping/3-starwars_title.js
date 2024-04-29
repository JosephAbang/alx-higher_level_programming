#!/usr/bin/node

// Import built in Node.js 'request' module
const req = require('request');

// Define endpoint url
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// Use reqtest module to perform GET request
req(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
