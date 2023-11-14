#!/usr/bin/node

const baseSquare = require('./5-square');

class Square extends baseSquare {
  charPrint (c) {
    let count = this.width;
    let text = '';
    while (count) {
      if (c) {
        text = text + c;
      } else {
        text = text + 'X';
      }
      count--;
    }
    count = this.height;
    while (count) {
      console.log(text);
      count--;
    }
  }
}

module.exports = Square;
