'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');
    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'closestNumber' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER a
 *  2. INTEGER b
 *  3. INTEGER x
 */

function closestNumber(a, b, x) {
    let n = Math.pow(a, b);

    let q = Math.floor(n / x);

    let lower = q * x;
    let upper = (q + 1) * x;

    if (Math.abs(n - lower) < Math.abs(n - upper)) {
        return lower;
    } else if (Math.abs(n - lower) > Math.abs(n - upper)) {
        return upper;
    } else {
        return Math.min(lower, upper);
    }
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const t = parseInt(readLine().trim(), 10);

    for (let tItr = 0; tItr < t; tItr++) {
        const firstMultipleInput = readLine().trim().split(' ');

        const a = parseInt(firstMultipleInput[0], 10);
        const b = parseInt(firstMultipleInput[1], 10);
        const x = parseInt(firstMultipleInput[2], 10);

        const result = closestNumber(a, b, x);

        ws.write(result + '\n');
    }

    ws.end();
}
