#!/usr/bin/node
console.log(isNaN(process.argv[2]) ? 'Not a number' : `my number: ${Math.floor(process.argv[2])}`);
