#!/usr/bin/node

if (process.argv[2]) {
  let x = 1;
  let y = 1;
  const num = process.argv[2];
  while (x <= num) {
    y *= x;
    x = x + 1;
  }
  console.log(y);
} else {
  console.log('1');
}
