// console.log(Math.PI);

// let x = (4.4);
// console.log(Math.round(x));

// let x = (6.4);
// function findRound(a){
//     return `The given function of round is : ${Math.round(a)}`
// }
// console.log(findRound(x));

// let arrFunc = () =>{
//     return Math.round(6.4);
// }
// console.log(arrFunc());

// let y = (a) => {
//     return Math.round(a);
// }
// console.log(y(x));

// let x = (4.4);
// let y = () => {
//     return Math.round(x);
// }
// console.log(y());


/////////// Math.pow()
// //////////////////////Math.pow(x, y) returns the value of x to the power of y:
// let por = (5, 7)
// console.log(Math.pow(8, 3));

function resultPow(x, y){
    return Math.pow(x, y);
}
console.log(resultPow(2, 3));

////// Math.sqrt()
// /////Math.sqrt(x) returns the square root of x:

// let x = 4.1
// console.log(Math.ceil(x))


//// Math.trunc()
//// Math.trunc(x) returns the integer part of x:
// let x = 5.1;
// console.log(Math.trunc(x));



///// Math.sign()
///// Math.sign(x) returns if x is negative, null or positive:
// console.log(Math.sign(98));
// console.log(Math.sign(0));
// console.log(Math.sign(-4));



///// Math.abs()
//// Math.abs(x) returns the absolute (positive) value of x:
// console.log(Math.abs(-4.7));



///// Math.sin()
///// Math.sin(x) returns the sine (a value between -1 and 1) of the angle x (given in radians).
///// If you want to use degrees instead of radians, you have to convert degrees to radians:
//// Angle in radians = Angle in degrees x PI / 180.
// console.log(Math.sin(90 * Math.PI / 180)); 
// console.log(Math.sin(50 * Math.PI / 100)); 



//// Math.cos()
//// Math.cos(x) returns the cosine (a value between -1 and 1) of the angle x (given in radians).
//// If you want to use degrees instead of radians, you have to convert degrees to radians:
//// Angle in radians = Angle in degrees x PI / 180.
//// Example
// console.log(Math.cos(0 * Math.PI / 180));     // returns 1 (the cos of 0 degrees)



/* Math.min() and Math.max()
Math.min() and Math.max() can be used to find the lowest or highest value in a list of arguments:
Example
let a = (0, 150, 30, 20);
console.log(Math.min(a));
Example
console.log(Math.max(0, 150, 30, 20, -8, -200));*/



// /*Math.random()
// Math.random() returns a random number between 0 (inclusive), and 1 (exclusive):
// Example
// console.log(Math.random());



// The Math.log() Method
// Math.log(x) returns the natural logarithm of x.
// The natural logarithm returns the time needed to reach a certain level of growth:
// Examples
// console.log(Math.log(1));
// console.log(Math.log(2));
// console.log(Math.log(3));



//// The Math.log2() Method
//// Math.log2(x) returns the base 2 logarithm of x.
//// How many times must we multiply 2 to get 8?
// console.log(Math.log2(8));



//// The Math.log10() Method
//// Math.log10(x) returns the base 10 logarithm of x.
//// How many times must we multiply 10 to get 1000?
// console.log(Math.log10(1000));



// JavaScript Math.random()
// Definition and Usage
// The Math.random() method returns a random number from 0 (inclusive) up to but not including 1 (exclusive).
// let x = Math.random();
// console.log(x);

// let x = Math.floor(Math.random() * 11);
// console.log(x);

// let x = Math.floor(Math.random() * 11);
// let primeNumber = 0
// for (let i = 0; i < 11; i+2){
//     x +=i 
// }
// console.log(x);


var a = 7;
var b = 10;
console.log(a&&b);


var a =7;
var b;
console.log(a&&b);


