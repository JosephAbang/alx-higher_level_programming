#!/usr/bin/node

const args = process.argv;

if (Number(`${args[2]}`)) {
  const num = parseInt(`${args[2]}`);
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
