#!/usr/bin/node

const arg = Math.floor(Number(process.argv[2]));

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    let line = '';
    for (let j = 0; j < arg; j++) {
      line = line + 'X';
    }
    console.log(line);
  }
}
