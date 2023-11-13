#!/usr/bin/node
function factorial (num) {
  if (isNaN(num) || num === 1) {
    return (1);
  } else {
    return factorial(num - 1) * num;
  }
}

console.log(factorial(parseInt(process.argv[2])));
