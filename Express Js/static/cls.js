class User{
    constructor(Name, Age, Country){
        this.Name = Name;
        this.Age = Age;
        this.Country = Country;
    }

    College(){
        this.email = "abc094@gmail.com"
        return "Dev Bhoomi Institute Of Technology"
    }

    getEmail(){
        return this.email;
    }
}

// var user1 = new User("Harshit", 25, "India");
// console.log(user1.College());
// console.log(user1.getEmail());

class user1 extends User{
    constructor(Name, Age, Country, City){
        super(Name, Age, Country);
        this.City = City;
    }

    static Hello(x){
        return "Hello" +" " + x.Name
    }
}

var person = new user1("Pravin", 25, "India", "Patna");
console.log(person);
console.log(user1.Hello(person));