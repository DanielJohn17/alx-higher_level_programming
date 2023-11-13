#!/usr/bin/node
const x = parseInt(process.argv[2]);
let s;
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    s = '';
    for (let j = 0; j < x; j++) {
      s += 'X';
    }
    console.log(s);
  }
}
