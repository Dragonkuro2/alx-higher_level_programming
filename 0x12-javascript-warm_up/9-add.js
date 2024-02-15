#!/usr/bin/node
const num1 = process.argv[2];
const num2 = process.argv[3];
function add (nb1, nb2) {
  console.log(nb1 + nb2);
}
add(Number(num1), Number(num2));
