/*let name = 'Adesuwa';
console.log(name);

let firstName='Sandra';
let lastName='Balogun'*/



let number= max(1, 2);
console.log(number);

function max(a, b){
    if (a > b) return a;
    else return b; 
}


console.log(isLandscape(800, 1000));

function isLandscape(width, height) {
    return (width > height); 
}

const output = fizzBuzz(15);
console.log(output);

function fizzBuzz(input) { 
    if (typeof input !== 'number')
    return 'Not a number';

    if (input % 3 === 0)
    return 'fizz';

    if (input % 5 === 0)
    return 'Buzz';

    if ((input % 3 === 0) && (input % 5 === 0))
    return 'fizzBuzz';

    return input; 8791
}

showStars(8);

function showStars(rows){
    for (let row = 1; row <= rows; row++) {
        let pattern = '';
        for (let i = 0; i < row; i++)
        pattern +='*';
        console.log(pattern);
    }
}

