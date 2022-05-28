// function myCurrying(a){
//     return function (b){
//         return function(c){
//             console.log(a, b, c);
//         };
//     };
// };
// myCurrying(6) (8) (3);

// let currying = (a) => (b) => (c) => (d) => a+b+c+d;
// console.log(currying (4) (7) (9) (3)) ;

// function sum (a){
//     return function (b){
//         var result = 'i love '.concat(a) + ' '.concat('and') + ' '. concat(b) + ' ' +'Cricket';
//         return result;
//     };
// };
// console.log(sum ("watching") ("playing"));

// var sum = function(a){
//     return function(b){
//         var result = `i love ${a} ${b}`;
//         return result;
//     }
// }
// console.log(sum ("playing") ("cricket"));

var currying = (m) =>(n) = (m*n);
