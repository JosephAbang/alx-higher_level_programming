#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !h || !w) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let count = this.width;
    let text = '';
    while (count) {
      text = text + 'X';
      count--;
    }
    count = this.height;
    while (count) {
      console.log(text);
      count--;
    }
  }
}

module.exports = Rectangle;
