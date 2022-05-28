// let complete = true;
// let prom = new Promise(function(resolve, reject){
//     if(complete){
//         resolve("I am sucessed");
//     }
//     else{
//         reject("I am failed");
//     }
// })
// console.log(prom);

// function myPromise(number){

//     return new Promise(function(resolve, reject){
//         if( number % 2 == 0){
//             resolve("This the even number.");
//         }
//         else{
//             reject("This is the odd number.");
//         }
//     });
// }
// console.log(myPromise(201));
/////////////////////////


// let complete = false;
// let prom = new Promise(function(resolve, reject){
//     if (complete){
//         resolve();
//     }
//     else{
//         reject();
//     }
// });

// prom.then(function(){
//     console.log("It is true!");

// });

// prom.catch(function(){
//     console.log("It is false!");
// });


// let myPromise  = new Promise(function(resolve, reject){
//     let x = 15;
//     if (x == 10){
//         resolve();
//     }
//     else if(x < 10){
//         console.log("x is not equal of 10!")
//     }
//     else{
//         reject();
//     }
// });

// myPromise.then(function(){
//     console.log("x is equal of 10!");
// });

// myPromise.catch(function(){
//     console.log("Error!");
// });

// let prom = new Promise(function(resolve, reject){
//     let x = 6;
//     if(x == 5){
//         resolve();
//     }
//     else{
//         reject();
//     }
// });

// let forResolve = ()=>{
//     console.log("ok")};

// let forReject=()=>{
//     console.log("not ok");
// };

// prom.then(forResolve);

// prom.catch(forReject);

// let myPromise = new Promise(function(resolve, reject){
//     setTimeout(function(){
//         resolve();
//     }, 5000);

//     console.log("Hello india");
// });

// let forResolve = ()=>{
//     console.log("Jai Shri Ram!");
// };
// myPromise.then(forResolve);

// let myPromise = new Promise(function(resolve, reject){
//     setTimeout(function(){
//         resolve();
//     }, 5000);
//     console.log("Hello india!");
// });

// myPromise.then(function(){
//     console.log("Jai Shri Ram!")
// });

// let myPromise = new Promise(function(resolve, reject){
//     setTimeout(myFunction, 5000);
//     function myFunction(){
//         console.log("Hello india!");
//     }
//     resolve();
// });

// myPromise.then(function(){
//     console.log("Jai shri ram!");
// });

// let prom = new Promise(function(resolve, reject){
//     console.log("Uploading data, Please wait..");
//     let name = "Harshiit";
//     setTimeout(()=>{
//         if (name == "Harshit"){
//             resolve();
//         }
//         else{
//             reject();
//         }
//     }, 9000);
// });

// prom.then(function(){
//     console.log("Name is Harshit!");
// });

// prom.catch(function(){
//     console.log("Error!");
// });


function myPromiseFunc (){   //Normal Function
    return new Promise(function(resolve, reject){   //Return Promise function
        console.log("Please wait.")
    setTimeout(()=>{            //We can use aysnchronous Function to set the keep on holding.
        let error = false;
        if(!error){
            console.log("Your Promise has been resolved");
            resolve();      //if problem has been resolved then call resolved function
        }
        else {
            console.log("Your Promise has been reject");
            reject();  //if aproblem not resolved rhen call reject method and reject the Promise. 
        }
    }, 5000);
 });
};

myPromiseFunc().then(function(){ //create a call function for resolved Promise
    console.log("Success");
});

myPromiseFunc().catch(function(){   //create a call function for reject Promise function.
    console.log("Rejected!.")
})

myPromiseFunc();