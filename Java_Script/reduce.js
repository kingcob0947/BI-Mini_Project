// let a1 = [2,7,5,8,9,4];
// let a2= a1.reduce((eccumulator, element, index, aar) => eccumulator + element);
// console.log(a2);

// let a3 = [2,7,5,8,9,4];
// let a4 = a3.reduce((eccumulator, element, index, arr) =>{
//     return eccumulator + element;
// })
// console.log(a4)

// const red = [12,3,6,4,0,4];
// const rud = red.reduce(reduce_function);
// function reduce_function(total, num){
//     return total - num;
// }
// console.log(rud);

// const red = [15,3,6,4,0,4];
// const rud = red.reduce((accumulated, num) => {
//     return accumulated - num;
// })
// console.log(rud);

// const red = [12,3,6,4,0,4];
// const rud = red.reduce((acumul, num) => acumul + num);
// console.log(rud)

// const red = [12,3,6,4,0,4,5];
// const rud = red.map((element) => element * 2) .filter((element) => element > 9)
//             .reduce((acculumated, element) => acculumated + element);
// console.log(rud);

// let a = [
//     ['a', 'b', 'c'],
//     ['d', 'e', 'f'],
//     ['g', 'h', 'i']
// ];

// let b = a.reduce((acculate, num) =>{
//     return acculate.concat(num);
// });
// console.log(a);
// console.log(b);

let char = ['A', 'B', 'A', 'C', 'B'];
let Chars = [...new Set(char)];

console.log(Chars);