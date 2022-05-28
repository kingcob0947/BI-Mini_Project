/* function firstFunction(){
//     console.log("Hello world")
// }

// function secondFunction(){
//     console.log("Hello India")
// }

// firstFunction();
// secondFunction();

function thirdFunction(value){
    value();
}
thirdFunction(firstFunction);*/



/*Sequence Control
Sometimes you would like to have better control over when to execute a function.
Suppose you want to do a calculation, and then display the result.
You could call a calculator function (myCalculator), save the result, and then call another function (myDisplayer) 
to display the result:
Example:-*/

/*function myfunc(some){
    return "Hello India";
}

function sumFunc(num1, num2){
    sum = num1 + num2;
    return sum;
}

let result = sumFunc(5, 5);
console.log(myfunc(result));*?

/*function myfunc(some){
    return "Hello India";
}

function sumFunc(num1, num2){
    sum = num1 + num2;
    myfunc(sum);
}
console.log(sumFunc(5, 5));*/

/*function show(a){
    console.log("i am show function of" + " " + a);
}
function myFunc(call){
    var b = 101;
    call(b);
}
myFunc(show);*/

//Asynchronous Callback ::-
// setTimeout(function myfunction){
//     console.log("I am show function");
// }, 5000);
// console.log("End");

const myFunction1 = ()=>{
    console.log("myFunction1 is starting");
}

const myFunction2 = ()=>{
    myFunction1();
    console.log("myFunction2 is ending")
}
myFunction2();