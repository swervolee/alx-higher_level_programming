#!/usr/bin/node

let arg = process.argv.slice(2);

arg = arg.map(x => Math.floor(Number(x)));

if (arg.length === 1 || arg.length === 0) {
  console.log(0);
} else {
  console.log(arg.slice().sort((a, b) => b - a)[1]);
}
