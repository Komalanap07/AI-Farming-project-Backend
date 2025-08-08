# import torch
# from torchvision import models, transforms
# from PIL import Image
# import os

# # 🚀 Set device
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# print(f"🔍 Using device: {device}")

# # 📂 Path to model and test folder
# model_path = "crop_disease_model.pth"
# test_dir = "Test"

# # 🏷️ Your class names (from training script)
# classes = ['American Bollworm on Cotton', 'Anthracnose on Cotton', 'Army worm', 'Becterial Blight in Rice',
#            'Brownspot', 'Common_Rust', 'Cotton Aphid', 'Flag Smut', 'Gray_Leaf_Spot', 'Healthy Maize',
#            'Healthy Wheat', 'Healthy cotton', 'Leaf Curl', 'Leaf smut', 'Mosaic sugarcane', 'RedRot sugarcane',
#            'RedRust sugarcane', 'Rice Blast', 'Sugarcane Healthy', 'Tungro', 'Wheat Brown leaf Rust',
#            'Wheat Stem fly', 'Wheat aphid', 'Wheat black rust', 'Wheat leaf blight', 'Wheat mite',
#            'Wheat powdery mildew', 'Wheat scab', 'Wheat___Yellow_Rust', 'Wilt', 'Yellow Rust Sugarcane',
#            'bacterial_blight in Cotton', 'bollrot on Cotton', 'bollworm on Cotton', 'cotton mealy bug',
#            'cotton whitefly', 'maize ear rot', 'maize fall armyworm', 'maize stem borer',
#            'pink bollworm in cotton', 'red cotton bug', 'thirps on  cotton']

# # 🔁 Same transform as used during training
# transform = transforms.Compose([
#     transforms.Resize((224, 224)),
#     transforms.ToTensor(),
# ])

# # 🧠 Load model
# model = models.mobilenet_v2(weights=None)
# model.classifier[1] = torch.nn.Linear(model.last_channel, len(classes))
# model.load_state_dict(torch.load(model_path, map_location=device))
# model = model.to(device)
# model.eval()

# # 🧪 Predict function
# def predict_image(img_path):
#     image = Image.open(img_path).convert("RGB")
#     image = transform(image).unsqueeze(0).to(device)

#     with torch.no_grad():
#         output = model(image)
#         _, predicted = torch.max(output, 1)

#     class_name = classes[predicted.item()]
#     return class_name

# # 🔍 Loop through test images
# print("🧪 Predictions:")
# for root, _, files in os.walk(test_dir):
#     for file in files:
#         if file.lower().endswith((".jpg", ".png", ".jpeg")):
#             path = os.path.join(root, file)
#             result = predict_image(path)
#             print(f"📸 {file} ➜ {result}")



import torch
from torchvision import models, transforms
from PIL import Image
import sys
import json

# 🚀 Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 📂 Model path
model_path = "ml/crop_disease_model.pth"  # <-- update if your path differs

# 🏷️ Class names
classes = ['American Bollworm on Cotton', 'Anthracnose on Cotton', 'Army worm', 'Becterial Blight in Rice',
           'Brownspot', 'Common_Rust', 'Cotton Aphid', 'Flag Smut', 'Gray_Leaf_Spot', 'Healthy Maize',
           'Healthy Wheat', 'Healthy cotton', 'Leaf Curl', 'Leaf smut', 'Mosaic sugarcane', 'RedRot sugarcane',
           'RedRust sugarcane', 'Rice Blast', 'Sugarcane Healthy', 'Tungro', 'Wheat Brown leaf Rust',
           'Wheat Stem fly', 'Wheat aphid', 'Wheat black rust', 'Wheat leaf blight', 'Wheat mite',
           'Wheat powdery mildew', 'Wheat scab', 'Wheat___Yellow_Rust', 'Wilt', 'Yellow Rust Sugarcane',
           'bacterial_blight in Cotton', 'bollrot on Cotton', 'bollworm on Cotton', 'cotton mealy bug',
           'cotton whitefly', 'maize ear rot', 'maize fall armyworm', 'maize stem borer',
           'pink bollworm in cotton', 'red cotton bug', 'thirps on  cotton']

# 🔁 Image transforms (same as training)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# 🧠 Load the model
model = models.mobilenet_v2(weights=None)
model.classifier[1] = torch.nn.Linear(model.last_channel, len(classes))
model.load_state_dict(torch.load(model_path, map_location=device))
model.to(device)
model.eval()

# ✅ Get image path from command line
if len(sys.argv) != 2:
    print(json.dumps({"error": "No image path provided"}))
    sys.exit(1)

image_path = sys.argv[1]

try:
    image = Image.open(image_path).convert("RGB")
    image_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image_tensor)
        _, predicted = torch.max(output, 1)

    predicted_class = classes[predicted.item()]
    print(json.dumps({ "prediction": predicted_class }))

except Exception as e:
    print(json.dumps({ "error": str(e) }))
