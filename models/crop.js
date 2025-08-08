const mongoose = require("mongoose");

const predictionSchema = new mongoose.Schema({
  imagePath: {
    type: String,
    required: true,
  },
  result: {
    type: String,
    required: true,
  },
  date: {
    type: Date,
    default: Date.now,
  },
});

module.exports = mongoose.model("Prediction", predictionSchema);
