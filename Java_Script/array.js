const car = ['safari', 'jaguaar', 'audy', 'toyota', '19'];
console.log(car);
console.log(Array.isArray(car));
console.log(car.length);

// const arr = [];
// arr[0] = "harshit",
// arr[1] = "ram",
// arr[2] = "bajrang"
// console.log(arr);
// console.log(Array.isArray(arr));

// const Car = {
//         Company: "TATA",
//         Model: "Safari",
//         Color: "DarkBlue",
//         Price: 2500000
//     };
//     console.log(Car);
//     console.log(Array.isArray(Car));

// const Car = {
//     tata : "safari",
//     kia : "sonet"
// };
// console.log(Array.isArray(Car));

// let newcar = new Array(1, 3, 5, "orange", "papaya", 3.5, true);
// console.log(Array.isArray(newcar));

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// console.log(fruits.toString);

// const fruits = ["orange", "papaya", "banana"];
// fruits.push=("kiwi");
// console.log(fruits);

// const fruit = ["Banana", "Orange", "Apple", "Mango"];
// let leng = fruit.push("Kiwi");
// console.log(leng);
    
// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// fruits.pop();
// console.log(fruits);

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// const popped_item = fruits.pop();
// console.log(popped_item);

// const fruits = ["Banana", "Orange", "Apple", "Mango"];

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// fruits.shift();
// console.log(fruits);

// let fruits = ["apple", "orange", "papaya", "kiwi"]
// let fruit = fruits.shift();

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// fruits.unshift("Lemon");
// console.log(fruits);

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// fruits.unshift("Lemon");
// console.log(fruits);
// console.log(fruits[1]);

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// fruits[fruits.length] = "Kiwi";
// console.log(fruits);

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// delete fruits[0];
// console.log(fruits);

// const a1 = [1,2,3,4,5];
// const a2 = [6,7,8,9,10];
// const a3 = a1.concat(a2);
// console.log(a3);

// let fruit1 = ["apple", "papaya", "orange"];
// let fruit2 = ["mango", "watermelon", "graphes"];
// let fruit3 = ["banana", "cherry", "pineapple", "laychee"];
// let fruit4 = fruit1.concat(fruit2, fruit3);
// console.log(fruit4);

// let a = [9,8,7,6];
// let b = ['a', 'b'];
// let c = a.concat(b, "D");
// console.log(c);

// const fruits = ["apple", "orange"];
// fruits.push("kiwi", "mango");
// console.log(fruits);

// let fruits = ["apple", "orangje", "mango", "papaya"];
// fruits.splice(2, 2, "kiwi", "lemon");
// console.log(fruits);

// let fruit = ["apple", "mango", "orange", "kiwi"];
// let fruits = fruit.slice(1, 2);
// console.log(fruits);
// console.log(fruit[0]);

// let arr = [1,2,3,4,5,6,7,8,9,0]
// console.log(arr.length-6);

// let fruits = ["apple", "mango", "orangge", "kiwi", "papaya"];
// for (let i = 0; i < fruits.length; i++){
//     console.log(fruits[i]);
// }

// let fruits = ["apple", "mango", "orangge", "kiwi", "papaya"];
// for (let element in fruits){
//     console.log(element);
// }

// text = [];
// for (i in fruits){
//     text += i;
//     console.log(text);

// let fruits = ["apple", "mango", "orangge", "kiwi", "papaya"];
// for (let element of fruits){
//     console.log(element);
// }

// let fruits = ["apple", "mango", "orangge", "kiwi", "papaya"];
// fruits.forEach(function(element, index, array){
//     console.log(element, index, array);

// });


// indexOf() Method : -
// let fruits = [1, 4, 2, 4, 3, 4, 5];
// console.log(fruits.indexOf(4, 2));

// let fruits = [1, 2, 1, 4, 1];
// console.log(fruits.indexOf(1, 3));

// let fruits = [1, 2, 1, 4, 1];
// console.log(fruits.indexOf(1, -1));

// includes() Method : -
// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// console.log(fruits.includes("Mango"));

// Start the search at position 3:

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// console.log(fruits.includes("Banana", 3));

// console.log(typeof{name:"Ram", age:"34"});

// console.log( false && 'cat' );



// true && false
// true && true

// let ages = [12,87,37,54,39,18];
// function checkAge(age){
//     return age > 18;
// }
// console.log(ages.find(checkAge));

// let age = [12,87,37,54,39,18]
// age.push(49, 25);
// console.log(age);


// let arrray1 = [12, 4, 6, 8, 10];
// let array2 = arrray1.map(arrayFunction);
// function arrayFunction(element, index, array){
//     return element * 2;
// }
// console.log(array2);

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// // for (let i = 0; i<1; i++){
// console.log(fruits.sort());
// // }

// const points = [40, 100, 1, 5, 25, 10];
// points.sort(function(a, b){
//     return a - b
// });
// console.log(points);

for (let index = 0; index < 20; index++){
    let element = index;
    console.log("this is the index number" +" " + element)
}
console.log("All done");