#!/usr/bin/node

const args = process.argv;
let count;
if (Number(args[2])) {
  let num = parseInt(args[2]);
  while (num > 0) {
    let text = 'x';
    count = parseInt(args[2]);
    while (count > 1) {
      text = text + 'x';
      count--;
    }
    console.log(text);
    num--;
  }
} else {
  console.log('Missing size');
}
