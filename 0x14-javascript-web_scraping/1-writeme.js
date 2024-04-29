#!/usr/bin/node

// Import built in Node.js 'fs' module
const fs = require('fs');

// Write contents to a file probvided as command line argument
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', error => {
  if (error) {
    console.error('Error writing the file:', error);
  }
});
