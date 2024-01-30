#!/usr/bin/node
/* FILE WRITE */

const fs = require('fs');

const path = process.argv[2];
const data = process.argv[3];

fs.writeFile(path, data, (err) => { if (err) throw err; });
