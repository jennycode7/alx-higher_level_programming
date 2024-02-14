#!/usr/bin/node

if (process.argv[2]) {
  const num = process.argv[2];
  if (isNaN(num)) {
    console.log('Missing size');
  } else {
      for (let i = 0; i < num; i++) {
        let y = 'X';
        for (let x = 0; x < num - 1; x++) {
          y += 'X';
	}
        console.log(y);
      }
  }
} else {
  console.log('Missing size');
}
