//1. You are provided with a number, "**N**". Find its factorial. sample input 5, output 120.
// function factorialSearch(n){
//     let factor = 1;
//     if (n < 0){
//         console.log("Error");
//     }
//     else{
//         for (i = 1; i <= n; i++){
//             factor = factor * i;
//         }
//         console.log(factor); 
//     }
// }
// factorialSearch(5);


//2. You are given with a number "N", find its cube.sample input 2. output 8.
// function myCube(n){
//     return(n**3);
// }
// console.log(myCube(2));


//3.The area of an equilateral triangle is ¼(√3a2) where "**a**" represents a side of the
//triangle. You are provided with the side "**a**". Find the area of the equilateral triangle.
// function areaTriangle(side){
//     let area = 0;
//     area = Math.sqrt(3)/4*side*side;
//     console.log(+area);
//  }
//  areaTriangle(20);

//4. You will be provided with a number. Print the number of days in the month
// function showMonthDays(m){
//     if (m <= 12){
//         return new Date(2022, m, 0).getDate();
//     }
//     else{
//         console.log("Error!")
//     }  
// }
// console.log(showMonthDay(4));
// console.log(showMonthDay(8));

//5. You are given with a number **A** i.e. the temperature in Celcius. Write a program to
//convert this into Fahrenheit.

// function Fahrenheit(A){
//     let temp = A;
//     let fahre_it = temp * 9 / 5 + 32;
//     let result = temp+'\xB0C is ' + fahre_it + ' \xB0F.';
//     console.log(result);
// }
// Fahrenheit(12);

//6. Write a code to get an integer N and print the sum of values from 1 to N.
// function sumOfnNumber(n){
//     let sum = 0;
//     for (let i = 1; i <= n; i++){
//         sum = sum + i;
//     }
//     console.log(sum);
// }
// sumOfnNumber(10);

//7. You are provided with a number "N", Find the Nth term of the series: 1 , 4, 9, 16, 25,36, 49, 64, 81, .......
// function findnTerm(n){
//     let nth_term = 1;
//     if ( n <= 0){
//         console.log("Error");
//     }
//     else{
//         for (let i = 1; i <= n; i++){
//             nth_term = i * i;
//         }
//         console.log(nth_term);
//     }
// }
// findnTerm(18);

//8. \- Let "A" be a string. Remove all the whitespaces and find it's length.
// function removeWhiteS(str){
//     if (str <= 0){
//         console.log("error")
//     }
//     else{
//     let trimstr = str.split(' ').join('');
//     console.log(trimstr.length)
//     }
// }
// removeWhiteS("Lorem Ipsum");

//11. Given an array of N elements.find the number of occurences of each character and
//print it in the decreasing order of occurences, if 2 or more number occurs the same
//number of times, print the numbers in decreasing order.

// let arr = ['4', '4', '3', '3', '8', '7'];
// function removeWhiteS(narray){
//     let new_set = new Set(narray);
//     let new_array = new Array(new_set);
//     console.log(new_array);
// }
// removeWhiteS(arr);

//12. Simi is learning about palindromic numbers. Her teacher gave him the task to count
//all palindromic numbers present in that range.Simi has told you about this and want
//your help. You design an algorithm in order to help simi.
//You will be given a number ‘n’
//Print the count of all palindromic numbers till ’n’(inclusive)
function palinDromes(n)
{
    return (5 * Math.pow(10, parseInt((n - 1) / 2)));
}
var n = 2;
console.log(palinDromes(n));


//15.You are given a postfix expression. Evaluate the given expression and print the result.
// function postFixFunc(exp){
//     let stack=[];
//     for(let i=0; i<exp.length; i++)
//     {
//         let c = exp[i];
//         if(! isNaN( parseInt(c) ))
//         stack.push(c.charCodeAt(0) - '0'.charCodeAt(0));
//         else
//         {
//             let val1 = stack.pop();
//             let val2 = stack.pop();
              
//             switch(c)
//             {
//                 case '+':
//                 stack.push(val2+val1);
//                 break;
                  
//                 case '-':
//                 stack.push(val2- val1);
//                 break;
                  
//                 case '/':
//                 stack.push(val2/val1);
//                 break;
                  
//                 case '*':
//                 stack.push(val2*val1);
//                 break;
//           }
//         }
//     }
//     return stack.pop();  
// }
// let exp="531*+9-";
// console.log("postfix evaluation: "+postFixFunc(exp));

 