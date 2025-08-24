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

// gcd helper
function gcd(a, b) {
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

function solve(a) {
    // remove duplicates
    let unique = [...new Set(a)];

    // if only one unique element -> cannot form valid subset
    if (unique.length === 1) return "NO";

    // compute gcd of all unique elements
    let g = unique[0];
    for (let i = 1; i < unique.length; i++) {
        g = gcd(g, unique[i]);
        if (g === 1) break; // early exit
    }

    return g === 1 ? "YES" : "NO";
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const t = parseInt(readLine().trim(), 10);

    for (let tItr = 0; tItr < t; tItr++) {
        const aCount = parseInt(readLine().trim(), 10);

        const a = readLine().trim().split(' ').map(x => parseInt(x, 10));

        const result = solve(a);

        ws.write(result + '\n');
    }

    ws.end();
}
