const fs = require('fs');

const input = fs.readFileSync('input_2.txt', 'utf8');

const splitInput = input.split("\n")
let checksum2 = 0
let checksum3 = 0

for (let id of splitInput) {
    let counts = {}
    for (let chr of id) {
        if (chr in counts) {counts[chr] += 1}
        else {counts[chr] = 1}
    }
    for (chr in counts) {
        if (counts[chr] == 2) {checksum2 += 1; break}
    }
    for (chr in counts) {
        if (counts[chr] == 3) {checksum3 += 1; break}
    }
}


console.log(`Final checksum is: ${checksum2 * checksum3}`)