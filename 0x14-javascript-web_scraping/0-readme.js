#!/usr/bin/node

// Import built in Node.js 'fs' module
const fs = require('fs');

// Read contents of file probvided as command line argument
fs.readFile(process.argv[2], 'utf-8', function (error, content) {
  if (error) {
    console.error('Error reading the file:', error);
  } else {
    console.log(content);
  }
});
