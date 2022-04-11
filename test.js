var age = prompt("Enter your age");
if(age < 18){
    console.log("You are not elligble for vote");

}else if(age => 18 && age <=80){
    console.log("You are elligble for vote");

}else if(age =>81 && age <= 100){
    console.log("Your age is very high");

}else{
    console.log("you input a wrong details");
}



