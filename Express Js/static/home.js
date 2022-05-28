let obj = {
    Name : "Pravin Singh",
    Age  : 25,
    City : "Patna",
    country : "India",
    full_details : function(){
        return `${this.Name}, ${this.Age}, ${this.City}, ${this.country}`;
    }
}
// console.log(obj);
console.log(obj.full_details());

function myfunc(a, b){
    return a * b;
}
console.log(myfunc(5, 4));
module.exports.func = myfunc;

module.exports.val = obj;