#!/usr/bin/node

const arg = Number(process.argv[2]);

if (!isNaN(arg)) { console.log(`My number: ${arg}`); }
