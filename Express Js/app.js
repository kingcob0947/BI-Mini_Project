// const express = require("express");
// const app = express();
// const port = 8000;
// app.get("/", (req, res) =>{
//     res.send("This is my first express web page");
// });

// app.get("/about", (req, res) =>{
//     res.send("This is my second webpage of express.js.");
// });

// app.listen(port, () =>{
//     console.log(`The application started successfully on ${port}`);
// });

const express = require("express");
const app = express();
const path = require('path');
const port = 8000;

//For serving static folder
app.use('/static', express.static('static'));

app.set('view engine', 'pug');
app.set('views', path.join(__dirname, 'views'));

app.get("/demo", (req, res) => {
    res.status(200).render("demo", {title: "Hello Pravin Singh", message : "Hello eveyone welcome to the on my pug page!"});
});

app.get("/", (req, res)=>{ 
    res.status(200).send("This is homepage of my first express app with Harry");
});

app.get("/about", (req, res)=>{
    res.send("This is about page of my first express app with Harry");
});

app.post("/about", (req, res)=>{
    res.send("This is a post request about page of my first express app with Harry");
});

app.get("/this", (req, res)=>{
    res.status(404).send("This page is not found on my website cwh");
});

app.listen(port, ()=>{
    console.log(`The application started successfully on port ${port}`);
});
