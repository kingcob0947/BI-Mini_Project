const data = [
    {name:'anurag', desigantion:'learner'},
    {name:'karan', desigantion:'learner'},
    {name:'omprakash', desigantion:'learner'},
    {name:'pradhan', desigantion:'learner'},
    {name:'srujan', desigantion:'learner'},
    {name:'pravin', desigantion:'learner'},
    {name:'sourabh', desigantion:'learner'},
    {name:'trupti', desigantion:'learner'}
    ]

let database = data.map(function(element, index) {

    let desire = 0   //manually added
    if(desire = index + 1){
    return  element .name + " " + element.desigantion + " " + desire;
    }
    else {

    let storej = {};
    storej[element.name] = element.desigantion;
    storej.age = element.name.length + 10;
    return storej;
    } 
   

    
})/*.filter(element =>{  this code for filtering
//     return element.age > 22; 
// });*/
console.log(database);
//const months = ['Jan', 'Feb', 'Mar', 'Apr'];
// let monthsIndex = months.map(function(month, index){   this code for example
//       let noneZeroIndex = index + 1;
//       return month + '-' + noneZeroIndex;