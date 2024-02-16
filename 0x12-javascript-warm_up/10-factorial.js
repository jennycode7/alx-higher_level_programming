#!/usr/bin/node

function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

if (process.argv[2]) {
  console.log(factorial(process.argv[2]));
} else {
  console.log('1');
}
