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
  while (b !== 0n) {
    let t = a % b;
    a = b;
    b = t;
  }
  return a;
}

function solve(n, k, s) {
  // prefix sum of ones
  let prefix = new Array(n + 1).fill(0);
  for (let i = 0; i < n; i++) {
    prefix[i + 1] = prefix[i] + (s[i] === '1' ? 1 : 0);
  }

  let validPairs = 0n;

  for (let i = 1; i <= n; i++) {
    if (s[i - 1] === '1') {
      let l = Math.max(1, i - k);
      let r = Math.min(n, i + k);
      let onesInRange = prefix[r] - prefix[l - 1];
      validPairs += BigInt(onesInRange);
    }
  }

  let total = BigInt(n) * BigInt(n);

  if (validPairs === 0n) return "0/1";

  let g = gcd(validPairs, total);
  return `${validPairs / g}/${total / g}`;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const t = parseInt(readLine().trim(), 10);

  for (let tItr = 0; tItr < t; tItr++) {
    const [n, k] = readLine().trim().split(' ').map(Number);
    const s = readLine().trim();
    const result = solve(n, k, s);
    ws.write(result + '\n');
  }

  ws.end();
}
