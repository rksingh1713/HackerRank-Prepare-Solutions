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
 * Complete the 'efficientJanitor' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts FLOAT_ARRAY weight as parameter.
 */

function efficientJanitor(weight) {
    // Sort weights
    weight.sort((a, b) => a - b);
    let trips = 0;
    let left = 0;
    let right = weight.length - 1;

    while (left <= right) {
        // If the lightest + heaviest fit in one trip
        if (weight[left] + weight[right] <= 3.0) {
            left++;   // use the lightest
            right--;  // use the heaviest
        } else {
            right--;  // send the heaviest alone
        }
        trips++;
    }

    return trips;
}


function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const weightCount = parseInt(readLine().trim(), 10);

    let weight = [];

    for (let i = 0; i < weightCount; i++) {
        const weightItem = parseFloat(readLine().trim());
        weight.push(weightItem);
    }

    const result = efficientJanitor(weight);

    ws.write(result + '\n');

    ws.end();
}