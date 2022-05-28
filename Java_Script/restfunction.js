/*Rest parameter is an improved way to handle function parameter, allowing us to more easily handle 
various input as parameters in a function. The rest parameter syntax allows us to represent an indefinite
number of arguments as an array. With the help of a rest parameter a function can be called with any number
of arguments, no matter how it was defined. Rest parameter is added in ES2015 or ES6 which improved the ability
to handle parameter.*/

// function restFunction(){
//     let sum = 0
//     for (let i in arguments){
//         sum += arguments[i];
//     }
//     console.log(sum);
// }
// restFunction(10, 20, 30);

// function restFunc(...input){
//     let total = 0;
//     for( let i of input){
//         total += i;
//     }
//     return total;
// }
// console.log(restFunc(2,6,8,9,5));

function myFunc(name, ...args){
    sum = 0;
    for (let i in args){
        sum += args[i];
    }
    console.log(sum);
    console.log(name);
}
myFunc("Pravin Singh", 10, 20, 30, 40);