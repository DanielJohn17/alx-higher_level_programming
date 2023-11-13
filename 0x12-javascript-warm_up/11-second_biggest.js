#!/usr/bin/node

let biggest = 0;
let i;
const arrayNum = [];

for (i = 2; i < process.argv.length; i++) {
  if (!isNaN(parseInt(process.argv[i]))) {
    arrayNum[i - 2] = parseInt(process.argv[i]);
  }
}

if (arrayNum.length > 1) {
  biggest = Math.max(...arrayNum);
  arrayNum[i] = -Infinity;
  biggest = Math.max(...arrayNum);
}

console.log(biggest);
