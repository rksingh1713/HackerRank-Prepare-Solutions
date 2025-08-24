'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on('end', function () {
  inputString = inputString.split('\n');
  main();
});

function readLine() {
  return inputString[currentLine++];
}

function gcd(a, b) {
  while (b !== 0) {
    let t = a % b;
    a = b;
    b = t;
  }
  return a;
}

function solve(a, b, c) {
  let num, den;

  den = a * b;

  if (c >= a + b) {
    num = den; // whole rectangle
  } else if (c <= Math.min(a, b)) {
    num = c * c;
    den = 2 * den;
  } else if (c <= a && c > b) {
    num = c * b - (b * b) / 2;
  } else if (c <= b && c > a) {
    num = c * a - (a * a) / 2;
  } else {
    // c > a && c > b && c < a + b
    num = a * b - ((a + b - c) * (a + b - c)) / 2;
  }

  // num, den may be fractional due to /2, multiply to clear denominators
  if (num % 1 !== 0) {
    num *= 2;
    den *= 2;
  }

  num = Math.round(num);
  den = Math.round(den);

  let g = gcd(num, den);
  num /= g;
  den /= g;

  return `${num}/${den}`;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const n = parseInt(readLine().trim(), 10);

  for (let nItr = 0; nItr < n; nItr++) {
    const firstMultipleInput = readLine().trim().split(' ');

    const a = parseInt(firstMultipleInput[0], 10);
    const b = parseInt(firstMultipleInput[1], 10);
    const c = parseInt(firstMultipleInput[2], 10);

    const result = solve(a, b, c);

    ws.write(result + '\n');
  }

  ws.end();
}
