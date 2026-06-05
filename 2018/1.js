const fs = require('fs');

const input = fs.readFileSync('input_1.txt', 'utf8');
//console.log(input)

const splitInput = input.split('\n')
//console.log(splitInput[0])

let frequency = 0

for (let i = 0; i < splitInput.length; i++) {
    frequency += Number(splitInput[i])
}

console.log(`Final frequency is: ${frequency}`)