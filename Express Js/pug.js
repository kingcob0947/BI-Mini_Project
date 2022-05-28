const http = require("http");
const express = require("express");
const app = express();
// const hostname = '127.0.0.1';
const port = 8000;
const path = require("path");

app.use('/static', express.static('express'));
app.set('view engine', 'pug');
app.set('views', path.join(__dirname, 'views'));
// app.get('/demo', (req, res)=>{
//     res.status(200).render('demo')
// });

app.get('/', (req, res)=>{
    const con = "This is the best website for learn pug!"
    const obj = {"title": "About Pug!", "content": con}
    res.status(200).render('index.pug', obj);
});

app.listen(port, () =>{
    console.log(`The application has been started on port No.${port}`);
});