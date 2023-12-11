#!/usr/bin/node

const arg = process.argv.slice(2);

const len = arg.length;

if (len === 0) {
  console.log('No argument');
} else if (len === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
