#!/usr/bin/node

const number = process.argv[2];

if (!isNaN(number)) {
  const argu = parseInt(number);
  console.log('My number: ' + argu);
} else {
  console.log('Not a number');
}
