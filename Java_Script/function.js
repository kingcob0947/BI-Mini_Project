// function javascript(){
//     var a = {
//         name: "harshit",
//         age: 25
//     };
//     console.log(a);
// }
// javascript();

// function myfunction(a, b){
//     var a = 5;
//     var b = 5;
//     console.log(a*b);
// }
// myfunction();

// function mufunction(a, b){
//     return a*b;
// }
// console.log(mufunction(4,8));


// let f_name = "pravin";
// let l_name = "singh";
// function myfunc(a, b){
//     return `${f_name} ${l_name}`;
// }
// console.log(myfunc(f_name, l_name));

// let x = myfunction(4, 6);
//  function myfunction(a, b){
//      return a*b;
//  }
//  console.log(x);

// function myfunc(name, thanks){
//     console.log(`Happy birthday ${name} and ${thanks}`);
// }
// myfunc("rahul", "thanks a lot")

// let person = {
//     name1: "pravin",
//     game: function(){
//         return "GTA";
//     }
// }
// console.log(person.game());

// {
//     const name = "pravin";
//     console.log(name);

// }

// function myfunc(y, z){
//     return y + z;
// }
// console.log(myfunc(12, 8));

// function myfunc(x, y){
//     if (y == undefined){
//         y = 2;
//     }
//     return x * y
// }
// console.log(myfunc(4));

// function myfunction(x, y=2){
//     if (x == undefined){
//         x = 5;
//     }
//     return x * y;
// }
// console.log(myfunction());

// function myfunc(a, b = 5){
//     return a * b;
// }
// console.log(myfunc(2));

// y = findMax(1, 123, 500, 115, 44, 88);

// function findMax() {
//   let max = -Infinity;
//   for (let i = 0; i < arguments.length; i++) {
//     if (arguments[i] > max) {
//       max = arguments[i];
//     }
//   }
//   return max;
// }
// console.log(findMax(y));

// x = sumAll(1, 123, 500, 115, 44, 88);

// function sumAll() {
//   let sum = 0;
//   for (let i = 0; i < arguments.length; i++) {
//     sum += arguments[i];
//   }
//   return sum;
// }
// console.log(sumAll(x));

// x = sumAll (65,87,2,34,87,9,4);
// function sumAll(){
//   let sum = 0;
//   for(let i = 0; i<arguments.length; i++){
//     sum += arguments[i];
//   }
//   return sum;
// }
// console.log(sumAll(x));

// let myobject ={
//   fname : "harshit",
//   lnane : "patel",
//   age : 25,
//   fullname : function(){
//     return this.fname + " " + this.lnane
//   } 
// }
// console.log(myobject.fullname());

// let myobj = {
//   name : "ram",
//   age : 25,
//   gender : "male",
//   fulldetauls : function(){
//     return this.name + " " + this.age+ " " +this.gender;
//   }
// }
// console.log(myobj.fulldetauls());

// let myobj = {
//   name : "ram",
//   age : 25,
//   gender : "male",
//   fulldetauls : function(){
//     return this
//   }
// }
// console.log(myobj.fulldetauls());

// function myfun(arg1, arg2){
//   this.first_name = arg1;
//   this.last_name = arg2;
// }
// let myob = new myfun("ravi", "teja");
// console.log(myob.first_name + " " + myob.last_name);

// Function call()method:-
// const person = {
//   fullname : function(){
//     return this.first_name + " " + this.last_name;
//   }
// }

// const person1 = {
//   first_name : "john",
//   last_name : "doe"
// }

// const person2 = {
//   first_name : "virat",
//   last_name : "kohli"
// }

// console.log(person.fullname.call(person1));
// console.log(person.fullname.call(person2));

// const person = {
//   fname : "abc",
//   lname : "xyz",
//   fullname : function(){
//     return this.fname + " " + this.lname;
//   }
// }

// const member = {
//   fname : "cde",
//   lname : "ijk"
// }
// console.log(fullname.person.fullname.bind(member));

// function myfunc(a, b){
//   let c = a*b;
//   console.log(c);
// }

// // let func = myfunc(5,4);
// // console.log(func);
// let func = myfunc(4,5);
// func;

// function myfunc(a, b){
//   return  c = a*b;
// }
// let func = myfunc(5, 2);
// console.log(func);

//Function Expression
// let functionexp = function(x= 8, y = 2){
//   return x*y;
// }
// console.log(functionexp());

// let funexp = function(x, y=1){
//   return `the total number of sum is: ${x +y}` 
// }
// console.log(funexp(9));

// console.log(sum());
// function sum(){
//   let a = 5; let b = 6;
//   return sum = a + b; 
// }

// let Drink = "cofee"
// function Cofee(x){
//   for (Brain in x){
//     if (Brain != "cofee"){
//       return "Keep Cooding";
//     }else{
//       return "Order cofee";
//     }
//   }
// }
// console.log(Cofee(Drink));
  

// function Sum(num){
//   let sum = 0;
//   for (let i in num){
//   sum = sum+i
//   }
//   console.log(sum);
// };
// console.log(Sum(9));


// function myfunc(n){
//   let sum = 0;
//   for (let i=1; i<n; i++){
//     sum +=i
//   }
//   console.log(sum);
// };
// console.log(myfunc(10));

// function processData(inputString) {
//   // This line of code prints the first line of output
//   console.log("Hello, World.");
  
//   // Write the second line of output that prints the contents of 'inputString' here.
//   console.log('Welcome to 30 Days of Code!');
// }
// processData("hello india");

// function display()  
// {  
//   console.log(10+20+"30");
//   console.log('10'+20+30);  
// }  
// display();  

/*int number;//Here, a number has an undefined value.  
Null value: A value that is explicitly specified by the keyword "null" is known as a null value. For example:

String str=null;//Here, str has a null value.  */
  
  

// function myFunc(par, strokes){
//   const names = ["Hole-in-one!", "Eagle", "Birdie", "Par", "Bogey", "Double Bogey", "Go Home!"]; 
//   if(strokes==0){
//     return names[0];
//   }
// }
// myFunc(4,5);

// function myfunc(){
//   console.log("Hello india");
//   console.log("good morning");
// };
// console.log("Testing Purpos.")
// myfunc();
// console.log("This is await function");


async function myfunc(){
  console.log("Hello india");
  console.log("good morning");
};
console.log("Testing Purpos.")
myfunc();
console.log("This is await function");