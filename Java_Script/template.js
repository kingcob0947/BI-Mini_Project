// let text = `Hello World!`;
// console.log(text)

// let firstName = "John";
// let lastName = "Doe";

// console.log(`${firstName} ${lastName}!`);

// let number = 6;
// let common =1;

// if (number < 0){
//     console.log("0! is not possible")
// }
// else if( number===0){
//     console.log(`${number} ! = 1`);
// }
// else{
//     for (let i  = 1; i<=number; i++){
//         common = i*common;
//     }
//     console.log(`${number}!= ${common}`);
// }

// let number = 6;
// let common = 1;
// if (number < 0){
//     console.log("0 ! not possible")
// }
// else if (number === 0){
//     console.log(`${number}! = 1`);
// }
// else{
//     for (let i=1; i<=number; i++){
//         common = i*common;
//     }
//     console.log(`${number} ! = ${common}`);
// }

{/* <p id="demo"></p>
      <script>
          const datas = [
              {name:"Ajay", Profession:"Engineer"},
              {name:"Anuj", Profession:"Engineer"}
          ];

          function getDatas(){
            setTimeout(() => {
              let output="";
              datas.forEach((data,index)=>{
                output+=`<li>${data.name}</li>`;
              })
              document.body.innerHTML=output
              
            }, 1000);
          }
          
          function createdata(newdata){
            return new Promise((resolve, reject) =>{
            setTimeout(() =>{
              datas.push(newdata);
              let error=true;
              if(!error){
                resolve();
              }
                else
                {
                  reject("This is rejection from netwrok");
                
              }
              
            }, 2000);
          })
        }
          // getDatas();
        createdata({name:"Karan", Profession:"software Engineer"}).then(getDatas)




        <p id="demo"></p>
      <script>
          const datas = [
              {name:"Ajay", Profession:"Engineer"},
              {name:"Anuj", Profession:"Engineer"}
          ];

          function getDatas(){
            setTimeout(() => {
              let output="";
              datas.forEach((data,index)=>{
                output+=`<li>${data.name}</li>`;
              })
              document.body.innerHTML=output
              
            }, 1000);
          }
          
          function createdata(newdata){
            return new Promise((resolve, reject) =>{
            setTimeout(() =>{
              datas.push(newdata);
              let error=true;
              if(!error){
                resolve();
              }
                else
                {
                  reject("This is rejection from network");
                
              }
              
            }, 2000);
          })
        }
          // getDatas();
        // createdata({name:"Karan", Profession:"software Engineer"}).then().catch(err => console.log(err))

       async function start(){
         await createdata({name:"Karan", Profession:"software Engineer"})
       } 
       start();


       navigator.getBattery().then(getBattery) => {
    console.log(battery)
})
 */}

 
