// let a, b, c;
// [a, b , c] = [1,2,3];
// console.log(a, b, c);

// let a, b;
// [a, b ] = [1,2];
// console.log(a, b);

// [a,b,c, ...d] = [1,2,3,4,5,6,7,8,9,7,4,3,9];
// console.log(a);
// console.log(b);
// console.log(c);
// console.log(d);

// function disTruct(a, b, ...d){
//     return a + b;
// }
// console.log(disTruct(12, 34, 48, 98, 23, 65));

let num = [1,2,3,4,5];
function myDistruc(p){
    return p;
}
let y = myDistruc(num);
[a,b,c] = y
console.log(a);
console.log(b);
console.log(c);