const connectDB = require('./db');
const express=require('express');
require('dotenv').config();
const cropRoutes = require('./routes/croproute');
const user = require('./routes/userroute');

const app=express();
app.use(express.json());
connectDB();
const port=5000;

app.use('/user', user); 
app.use('/crop', cropRoutes);

app.listen(port,()=>{
    console.log(`server is listening on port ${port} `);
})