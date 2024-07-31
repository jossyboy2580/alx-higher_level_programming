#!/usr/bin/node
/**
 * A script to write some text into a file
 */

const fs = require('fs');

if (process.argv.length < 3) {
  console.error('Usage: <program> <destination_file> <content>');
  process.exit(1);
}

const fileName = process.argv[2];
const content = process.argv[3];

fs.writeFile(fileName, content, (err) => {
  if (err) {
    console.log(err);
  }
});
