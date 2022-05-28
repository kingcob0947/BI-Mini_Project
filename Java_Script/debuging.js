// function debugFunc(){
//     let star = 5;
//     for (i = 0; i < star; i++){
//         console.log("*");
//     }
// }
// debugFunc();

// function pyramid(n) {
//     debugger;
//     for (let i = 1; i <= n; i++) {
//        let str = ' '.repeat(n - i);
//        let str2 = '*'.repeat(i * 2 - 1);
//        console.log(str + str2 + str);
//     }
//  }
 
//  pyramid(5);

//  function generatePyramid() {
//     var totalNumberofRows = 5;
//     var output = '';
//     for (var i = 1; i <= totalNumberofRows; i++) {
//         for (var j = 1; j <= i; j++) {
//             output += j + '  ';
//         }
//         console.log(output);
//         output = '';
//     }
// } generatePyramid();

n = 5;
for (i =0; i <n; i++){
    for (j = n-1; j >= i * j; j--){
        console.log("");
    }
     for (k = 1; k <=n; k++){
         console.log("*")
     }
}