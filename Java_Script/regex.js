// let a = /harry/;
// console.log(a)

// let text = "welcome to my page";
// console.log(text.search("page"));

// let text = "welcome to my page";
// console.log(text.search(/page/));


// let text = "welcome to my page";
// console.log(text.replace(/page/, "webpage"));

// let text = "welcome to my page";
// console.log(text.replace(/page/i, "webpage"));

// let text = "welcome to mypage pravin";
// let reg = /pravin singh/
// console.log(reg.exec(text));

// let str = "My name is pravin singh";
// let name = /My/
// console.log(name.exec(str));

// let text = "this is my pen and this is your pen";
// let reg = /this/g;
// console.log(reg.exec(text));
// console.log(reg.exec(text));

// let text = "\nIs th\nis it?";
// let result = text.match(/^is/m);
// console.log(result);

// text = "Is this your number ? if not, then what is your number?"
// function myRegExp(tex){
//     console.log(tex.match(/is/i));
// }
// myRegExp(text);

// text = "\nis this your number ?\n if it is not, then what \nis your number?"
// function myRegExp(tex){
//     console.log(tex.match(/is/m));
// }
// myRegExp(text);

// let text = "what's your name";
// let testR = /u/;
// console.log(testR.test(text));
// console.log(testR.test("What is your name"));

let text = "this is your name";
let testR = /is/;
console.log(text.match(testR));