// console.log("This is the date method");

// // let d = new Date();
// // let dates = d;
// // console.log(d);

// // const d = new Date(2018, 16);
// // console.log(d);

// const d = new Date("October 13, 2014 11:13:00");
// console.log(d);

function monthInDays(month){
    if (month <= 12){
        return new Date(2022, month, 0). getDate();
    }
    else{
        console.log("Error!")
    }
}
console.log(monthInDays(1));
console.log(monthInDays(2));
console.log(monthInDays(3));
console.log(monthInDays(4));
console.log(monthInDays(5));
console.log(monthInDays(6));
console.log(monthInDays(7));
console.log(monthInDays(8));
console.log(monthInDays(9));
console.log(monthInDays(10));
console.log(monthInDays(11));
console.log(monthInDays(12));