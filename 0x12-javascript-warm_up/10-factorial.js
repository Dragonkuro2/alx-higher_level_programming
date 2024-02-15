#!/usr/bin/node
let result = 1;
const arg = Number(process.argv[2]);
function fuctorial (number) {
  if (number == 0) {
    return (1);
  } else {
      return (number * fuctorial(number - 1));
  }
}

if (isNaN(arg)) {
  console.log(1);
} else {
  console.log(fuctorial(arg));
}
