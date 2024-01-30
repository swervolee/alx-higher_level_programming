#!/usr/bin/node
/* FILE READING */

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, inputD) => {
  if (err) throw err;
  console.log(inputD.toString());
});
