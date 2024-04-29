#!/usr/bin/node

// Import the built-in Node.js 'fs' module
const fs = require('fs');

// Import built in Node.js 'request' module
const req = require('request');

req(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
