const express = require("express");
const router = express.Router();
const multer = require("multer");
const { predictDisease } = require("../controllers/cropcontroller");

// Configure multer for image upload
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, "uploads/");  // Make sure this folder exists
  },
  filename: (req, file, cb) => {
    const uniqueName = `${Date.now()}-${file.originalname}`;
    cb(null, uniqueName);
  }
});

const upload = multer({ storage });

// POST /api/predict
router.post("/predict", upload.single("image"), predictDisease);

module.exports = router;
