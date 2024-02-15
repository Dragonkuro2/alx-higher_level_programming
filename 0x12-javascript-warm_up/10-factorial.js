#!/usr/bin/node
let result = 1;
const arg = Number(process.argv[2]);
if (isNaN(arg)) {
  console.log(1);
} else {
  for (let i = arg; i > 0; i--) {
    result *= i;
  }
  console.log(result);
}
