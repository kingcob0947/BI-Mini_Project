// let arr = [1,2,3,4,5,6,7,8,9];
// let new_arr = arr.map((current_element, index, arre) => {
//      return current_element * 2;;

// })
// console.log(new_arr);

// let a = [10,2,3,1,23,40,52,87];
// let a1 = a.map((element, index, ar) =>{
//     return `index no : ${index} element: ${element*2} array: ${ar}  `
// }) 
// console.log(a);
// console.log(a1);

// let arr1 = [25,36,49, 64, 81];
// let arr2 = arr1.map((Element) => {
//     return Math.sqrt(Element);
// })
// console.log(arr2);

// let arr1 =[2, 3, 4, 6, 8];
// let arr2 = arr1.map((element) =>{
//     return element*2; 
    
// }) .filter((element) =>{
//     return element > 10;
// })
// console.log(arr2);

// let arr3 =[2, 3, 4, 7, 8];
// let arr4 = arr3.map((element) => element*2).filter((element) => element > 10).reduce((eccumulator, element) =>{
//     return eccumulator + element;
// });
// console.log(arr4);

// let x = [16, 4, 9, 81, 12, 20];
// let y = x.map((element, inndex, array) => {
//     return Math.sqrt(element);
// })
// console.log(y);

// let x = [16, 4, 9, 81, 12, 20];
// let y = x.map((element) => Math.sqrt(element))
// console.log(y);

// let x = [16, 4, 9, 81, 12, 20];
// let y = x.map((element) => {
//     return element*2;
//  })/*.filter((element) => {
// //     return element > 10
// // })*/
// console.log(y);

// let person = [
//     {
//         name : "pravin singh",
//         age : 25,
//         dept : "Software engineer",
//         company : "Google"
//     }
// ];
// person.map(getFullDetails);
// function getFullDetails(element){
//     return `${element}`
// }

// let a = [6,9,5,4,4,9];
// let b = a.map(test);
// function test(iteam){
//     return iteam * 10;
// }
// console.log(b);

// const ao = [
//      {first_name : "Yahho"},
//      {last_name : "baba"}
// ]
// const bo = ao.map(myfunc);
// function myfunc(x){
//     return x.first_name;
// }
// console.log(bo);

// let a  = [1,2,3,4,5];
// let b = a.map((element) => element * 4);
// console.log(b);

// let a = [3,4,9,6];
// let b = a.map((element, index, array) =>{
//     return `Index No : ${index}, element : ${element*3}, array : ${array}`;
// });
// console.log(b);

// let a = [2,3,4,5];
// let b = a.map((element, index, array)=>element * 2);

// let b = a.map((element, index, array) =>{
//     return  element * 3;
// })
// console.log(b);

// let b = a.map(mapFunction);
// function mapFunction(element, index, array){
//     return `Index No of : ${index}, element : ${element*4}, array : ${array}`
// }
// console.log(b);

// const data = [
//     {name:'anurag', desigantion:'learner'},
//     {name:'karan', desigantion:'learner'},
//     {name:'omprakash', desigantion:'learner'},
//     {name:'pradhan', desigantion:'learner'},
//     {name:'srujan', desigantion:'learner'},
//     {name:'pravin', desigantion:'learner'},
//     {name:'sourabh', desigantion:'learner'},
//     {name:'trupti', desigantion:'learner'}
//     ]

// const database = data.map(element => {
//     const container = {};
//     container[element.name] = element.desigantion;
//     container.age = element.name.length * 4;
//     return container;
// });
// console.log(database);
// // document.write(database);

// for (let i = 0; i < data.length; i++){
//     console.log(data[i]);
// }

let list = [2,3,4,5,6];
let maP = list.map(x=> x*2)
console.log(maP);