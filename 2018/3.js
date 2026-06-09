const fs = require('fs');
const input = fs.readFileSync('input_3.txt', 'utf8');

const splitInput = input.split("\n");

//interpret the claims
let claims = []
for (line of splitInput) {
    const claim = {};
    const lineDetails = line.split(" ");
    claim.no = lineDetails[0].slice(1);
    const offsets = lineDetails[2].split(",");
    claim.xOffset = Number(offsets[0]);
    claim.yOffset = Number(offsets[1].slice(0,offsets[1].length-1));
    const dimensions = lineDetails[3].split("x");
    claim.width = Number(dimensions[0]);
    claim.height = Number(dimensions[1]);
    claim.squares = new Set()
    claims.push(claim);
}
// claims = claims.slice(0,2)



let claimedSquares = [];
let overlaps = new Set();
//log claims on the fabric
for (claim of claims) {
    let unique = true
    const x_end = claim.xOffset + claim.width
    const y_end = claim.yOffset + claim.height
    for (let x = claim.xOffset; x < x_end; x++) {
        for (let y = claim.yOffset; y < y_end; y++) {
            let claimText = `${x}.${y}`
            claim.squares.add(claimText)
            if (claimedSquares.includes(claimText)) {overlaps.add(claimText)}
            else {claimedSquares.push(claimText)}
        }
    }
    console.log(`Processed Claim #${claim.no}`)
}


for (claim of claims) {
    const pleaseBeZero = overlaps.intersection(claim.squares)
    if (pleaseBeZero.size == 0) {console.log(`Claim #${claim.no} does not overlap!`); break}
}

console.log(`${overlaps.size} Squares of fabric are overbooked!`)