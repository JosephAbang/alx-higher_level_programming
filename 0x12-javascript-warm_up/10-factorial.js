#!/usr/bin/node

const args = process.argv;

const fact = parseInt(args[2]);
function factorial (a) {
  if (!a) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

console.log(factorial(fact));
