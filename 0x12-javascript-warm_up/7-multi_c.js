#!/usr/bin/node

if (process.argv[2]) {
  const num = process.argv[2];
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
