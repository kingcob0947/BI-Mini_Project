// let a = [7,9,4,6,0,2];
// let b = a.filter(test);
// function test(x){
//     return x > 4;
// }
// console.log(b);

// let a = [7,9,4,6,0,2];
// let b = a.filter(test);
// function test(x){
//     return x > 4 && x < 9 ;
// }
// console.log(b);

let age = [10,25, 15, 60, 70, 45, 18];
let ages = age.filter((ag) =>{
    return ag > 18;
});

// });
// console.log(ages);

// let age = [24,18,10,30,60, 35];
// let ages = age.map((element) =>{
//     return element*2;
// }).filter((element) =>{
//     return element > 50;
// })
// console.log(ages);

// let ag1 = [12, 45, 76, 30, 23];
// let ages1 = ag1.map((element) => element * 2).filter((element) => {
//        return element > 50;
// })
// console.log(ages1);

// let = 100;
// let prime = []
// for (i = 1; i < 100; 1+2){
//   if (i % 1 = 1){
//     ret
// }
// }


// function isPrime(num) {

//   for(let i = 2; i < num; i++)

//     if(num % i === 0) return false;

//   return num > 1;

// }
// console.log(isPrime(100));


function isPrime(num) {

  if (num === 2) {

    return true;

  } else if (num > 1) {

    for (var i = 2; i < num; i++) {

      if (num % i !== 0) {

        return true;

      } else if (num === i * i) {

        return false

      } else {

        return false;

      }

    }

  } else {

    return false;

  }

}

console.log(isPrime(121));