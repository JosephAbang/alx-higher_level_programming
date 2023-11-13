#!/usr/bin/node

const args = process.argv;

const newArr = [];
let i = 2;
let j = 0;
let max1;
let max2;

while (args[i]) {
  newArr[j] = parseInt(args[i]);
  i++;
  j++;
}

if ((j === 1) || !(args[2])) {
  console.log(0);
} else {
  i = 0;
  max1 = newArr[1];
  while (newArr[i]) {
    if (newArr[i] > max1) {
      max1 = newArr[i];
    }
    i++;
  }

  i = 0;
  max2 = 0;
  while (newArr[i]) {
    if ((newArr[i] > max2) && (newArr[i] !== max1)) {
      max2 = newArr[i];
    }
    i++;
  }

  console.log(max2);
}
