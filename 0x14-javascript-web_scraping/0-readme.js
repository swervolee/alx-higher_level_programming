#!/usr/bin/node
/* FILE READING */

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err) => console.error(err));
