const mongoose = require('mongoose');
require('dotenv').config();
// 5cWsje6sEuPBPrLu
// komalanap07
// mongodb+srv://komalanap07:<db_password>@cluster0.yphefxv.mongodb.net/
// mongodb+srv://komalanap07:<db_password>@cluster0.yphefxv.mongodb.net/
const connectDB = async () => {
  try {
    await mongoose.connect(process.env.MONGO_URI);
    console.log('✅ MongoDB connected');
  } catch (error) {
    console.error('❌ MongoDB connection error:', error.message);
    process.exit(1);
  }
};

module.exports = connectDB;
