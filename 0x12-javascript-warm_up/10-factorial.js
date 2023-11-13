#!/usr/bin/node
function factorial (num) {
  let multiple = 1;
  if (isNaN(num) || num === 1) {
    return (1);
  } else {
    for (let i = num; i > 0; i--) {
      multiple *= i;
    }
    return (multiple);
  }
}

console.log(factorial(parseInt(process.argv[2])));
