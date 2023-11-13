#!/usr/bin/node

const args = process.argv;
if (args[2]) {
  let num = parseInt(args[2]);
  while (num !== 0) {
    console.log('C is fun');
    num--;
  }
} else {
  console.log('Missing number of occurrences');
}
