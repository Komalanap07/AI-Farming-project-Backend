const { exec } = require("child_process");
const Prediction = require("../models/crop");

const predictDisease = async (req, res) => {
  try {
    console.log("Uploaded file:", req.file);

    if (!req.file) {
      return res.status(400).json({ error: "No image uploaded" });
    }

    const imagePath = req.file.path;

    // Run the Python script
    exec(`python ml/detect.py ${imagePath}`, async (error, stdout, stderr) => {
      if (error) {
        console.error("❌ Python Error:", stderr);
        return res.status(500).json({ error: "Python script error", details: stderr });
      }

      try {
        const output = JSON.parse(stdout);

        if (output.error) {
          return res.status(500).json({ error: "Model failed", details: output.error });
        }

        const result = output.prediction;

        // Save to MongoDB
        const prediction = new Prediction({
          imagePath,
          result,
        });

        await prediction.save();

        // Send response
        res.json({ result });

      } catch (jsonErr) {
        console.error("❌ JSON Parse Error:", jsonErr);
        res.status(500).json({ error: "Invalid response from Python script" });
      }
    });
  } catch (err) {
    console.error("❌ Server Error:", err);
    res.status(500).json({ error: "Server error" });
  }
};

module.exports = { predictDisease };
