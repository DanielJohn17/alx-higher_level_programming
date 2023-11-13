#!/usr/bin/node
function factorial (num) {
  if (isNaN(num) || num === 1) {
    return (1);
  } else {
    let multiple = 1;
    for (let i = num; i > 0; i--) {
      multiple *= i;
    }
    return (multiple);
  }
}

console.log(factorial(parseInt(process.argv[2])));
