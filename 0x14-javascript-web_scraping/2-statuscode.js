#!/usr/bin/node

// Import built in Node.js 'request' module
const req = require('request');

// Use the 'request' module to perfprm an HTTP GET request to the URL
req.get(process.argv[2]).on('response', function (response) {
  // Sety up event listener for response and print status code
  console.log(`code: ${response.statusCode}`);
});
