#!/usr/bin/node

const Rectangle = require('./5-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let line = '';
        for (let j = 0; j < this.width; j++) {
          line = line + c;
        }
        console.log(line);
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        let line = '';
        for (let j = 0; j < this.width; j++) {
          line = line + 'X';
        }
        console.log(line);
      }
    }
  }
};
