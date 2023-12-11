#!/usr/bin/node

const num = Math.floor(Number(process.argv[2]));

function factorial (num) {
  if (isNaN(num)) {
    return 1;
  }

  if (num === 1) {
    return 1;
  }

  return num * (factorial(num - 1));
}

console.log(factorial(num));
