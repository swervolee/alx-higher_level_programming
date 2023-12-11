#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

const a = Math.floor(Number(process.argv[2]));
const b = Math.floor(Number(process.argv[3]));

console.log(add(a, b));
