#!/usr/bin/node

function add (a, b) {
  const result = parseInt(a) + parseInt(b);
  console.log(result);
}

if (process.argv.length > 1) {
  const x = process.argv[2];
  const y = process.argv[3];
  add(x, y);
} else {
  console.log('NaN');
}
