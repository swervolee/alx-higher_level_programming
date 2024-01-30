#!/usr/bin/node
/* STREAMING TO A FILE */

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url).pipe(fs.createWriteStream(filePath));
