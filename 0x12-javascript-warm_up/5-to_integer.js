#!/usr/bin/node

const number = process.argv[2];

if (!isNaN(number)) {
  const argu_2 = parseInt(number);
  console.log('My number: ' + argu_2);
} else {
  console.log('Not a number');
}
