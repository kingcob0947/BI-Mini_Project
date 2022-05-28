// const person = {f_name:"Harshit", l_name:"Patel", age: 25};
// console.log(person);

// const Car = {
//     Company: "TATA",
//     Model: "Safari",
//     Color: "DarkBlue",
//     Price: 2500000
// };
// console.log(Car);

// const Car = {
//     Company: "TATA",
//     Model: "Safari",
//     Color: "DarkBlue",
//     Price: 2500000,
//     FullDetails: function() {
//         return this.Company + " " + this.Model + " " + this.Color;
//     }
// };
// console.log(Car);

// const person = {
//     firstName: "John",
//     lastName : "Doe",
//     id       : 5566,
//     fullName : function() {
//       return this.firstName + " " + this.lastName;
//     }
//   };
//   console.log(person.firstName);

// let college = {
//   College_Name : "Dev Bhoomi Institute of technology",
//   Address : "Dehradun",
//   Department : "Master Of Computer Application",
//   Full_Details : function (){
//     return this.College_Name + " " + this.Address + " " + this.Department
//   }
// }
// console.log(college.Full_Details());



/*What is this?
In JavaScript, the this keyword refers to an object.
Which object depends on how this is being invoked (used or called).
The this keyword refers to different objects depending on how it is used:
In an object method, this refers to the object.
Alone, this refers to the global object.
In a function, this refers to the global object.
In a function, in strict mode, this is undefined.
In an event, this refers to the element that received the event.
Methods like call(), apply(), and bind() can refer this to any object.
Note
this is not a variable. It is a keyword. You cannot change the value of this.*/

// Adding a Property to an Object
// Adding a new property to an existing object is easy:

// let Person = {
//   Name : "Pravin Singh",
//   Age : 25,
//   Gender : "M",
//   Address : "Patna",
//   Full_Details : function(){
//     return this.Name + ", " +  this.Age + ", " + this.Gender + ", " + this.Address
//   }
  
// }
// Person.Pincode = 804453
// console.log(Person.Pincode);

function createStudent(id, name, dept){
  let Student = {
    student_id : id,
    student_name : name,
    student_dept : dept,
    
    student_full_details : function(){
      console.log(`${this.student_id}, ${this.student_name}, ${this.student_dept}`);
    }
  }
  return Student;
}
console.log(createStudent(1, "Pravin Singh", "Computer Application"));
