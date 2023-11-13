#!/usr/bin/node
function factorial (num) {
  if (isNaN(num) || num === 1) {
    console.log('1');
  } else {
    let multiple = 1;
    for (let i = num; i > 0; i--) {
      multiple *= i;
    }
    console.log(multiple);
  }
}

factorial(parseInt(process.argv[2]));
