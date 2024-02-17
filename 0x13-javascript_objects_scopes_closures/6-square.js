#!/usr/bin/node
class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let rec = '';
        for (let j = 0; j < this.width; j++) {
          rec += c;
        }
        console.log(rec);
      }
    }
  }
}
module.exports = Square;
