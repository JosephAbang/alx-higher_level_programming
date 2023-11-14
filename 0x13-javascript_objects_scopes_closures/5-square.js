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

  rotate () {
    const tempWidth = this.width;
    const tempHeight = this.height;
    this.height = tempWidth;
    this.width = tempHeight;
  }

  double () {
    this.height = this.height * 2;
    this.width *= 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.width = size;
    this.height = size;
  }
}

module.exports = Square;
