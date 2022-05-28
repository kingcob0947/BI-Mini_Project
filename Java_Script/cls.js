// class student{
//     constructor(name, age, city){
//         this.myname = name;
//         this.myage = age;
//         this.mycity = city;
//     }

//     full_details(){
//         return`my name is ${this.myname}, i am ${this.myage} old, and i am from ${this.mycity}`;
//     }
// }
// let student1 = new student("pravin", 25, "patna");
// console.log(student1.full_details());
// console.log(student1);

// class Car{
//     constructor(name, year){
//         this.carname = name;
//         this.caryear = year;
//     }

//     age(){
//         let date = new Date();
//         return date.getFullYear() - this.caryear;
//     }
// }

// let mycar = new Car("Jaguaar", 2010);
// console.log(mycar.age());

// class Car {
//     constructor(name, year) {
//       this.name = name;
//       this.year = year;
//     }
//     age(x) {
//       return x + this.year;
//     }
//   }
//   let mycar = new Car("safari", 2004);
  // console.log(mycar.age(4));

  // class Car{
  //   constructor(name, year){
  //     this.name = name;
  //     this.year = year;
  //   }

  //   age(x){
  //     return x - this.year
  //   }
  // }
  // let date = new Date();
  // let year = date.getFullYear();

  // let mycar = new Car("jaguaar", 2005);
  // console.log(mycar.age(year));

  // class person{
  //   constructor(name, age, gender){
  //     this.name = name;
  //     this.age = age;
  //     this.gender = gender;
  //   }

  //   details(){
  //     return `the person name is ${this.name}, and ${this.age} year old and his gender is ${this.gender}`;
  //   }
  // }

  // class member extends person{
  //   constructor(name, age, gender, city){
  //   super(name, age, gender);
  //   this.city = city;
  //   }

  //   full_details(){
  //     return `the person name is ${this.name}, and ${this.age} year old his gender is ${this.gender}
  //     and he is from ${this.city}`;
  //   }
  // }

  // let person1 = new member("Thapa", 26, "Male", "ddn");
  // console.log(person1.details());
  // console.log(person1.full_details());

  // class person{
  //   constructor(name){
  //     this.name = name;
  //   }

  //   static hello(){
  //     return "hello";
  //   }
  // }

  // let p1 = new person("pravin");
  // console.log(person.hello());

// class person{
//   constructor(name){
//     this.name = name;
//   }

//   static hello(n){
//     return "hello" + " " + n.name;
//   }
// }

// let p1 = new person("pravin");
// console.log(person.hello(p1));

// class person{
//   constructor (name, age){
//     this.name = name;
//     this. age = age;
//   }
//   fullname(){
//     return this.name + " " +  this.age;
//   }
// }

// let person1 = new person("pravin", 25);
// console.log(person1.fullname());

class car{
  constructor(model, price){
    this. model = model;
    this. price = price;
  }

  fulldetails(){
    return `car model is ${this.model} and total price is ${this.price}`
  }

  static hello1(x){
    return "hello" + " " + x.model
  }
}

class car1 extends car{
  constructor(model, price, year){
    super(model, price);
    this.year = year;
  }

  full_details(){
    return `the car model is ${this.model}, the car price is ${this.price}, and bought in ${this.year}`;
  }

  static hello(){
    return "this is a static method"
  }
}

let c1 = new car1("Jaguaar", 8000000, 2015);
console.log(car1.hello1(c1));
console.log(c1.fulldetails());
console.log(c1.full_details());