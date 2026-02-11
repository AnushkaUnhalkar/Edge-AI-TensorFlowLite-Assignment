🚀 Mobile & Edge AI Project
TensorFlow Lite Model Conversion & Edge Deployment (Raspberry Pi Simulation)

📌 Project Overview
This assignment demonstrates:
✅ Converting a TensorFlow model to TensorFlow Lite
✅ Running a .tflite model locally
✅ Simulating Edge AI execution (Raspberry Pi environment)
✅ Performing inference using TensorFlow Lite
✅ Comparing performance between PC and Raspberry Pi

🔹 PART A – Project 1
TensorFlow Model Conversion to TensorFlow Lite

🎯 Objective
Convert a TensorFlow SavedModel into a lightweight .tflite model for edge deployment.

📂 Project Structure
Mobile_Edge_AI_Project/
│
├── mobilenet_saved_model/
├── mobilenet_model.tflite
├── step1_load_model.py
├── step2_convert_tflite.py
├── step3_test_tflite.py
├── raspberry_pi_simulation.py
├── requirements.txt
└── README.md

🛠️ Step 1 – Load TensorFlow Model
File: step1_load_model.py
Loads MobileNet model
Verifies model structure
Confirms successful loading

Run:
python step1_load_model.py

🔄 Step 2 – Convert to TensorFlow Lite
File: step2_convert_tflite.py
Converts SavedModel → .tflite
Optimizes model for edge devices
Saves file as mobilenet_model.tflite

Run:
python step2_convert_tflite.py

🧪 Step 3 – Test TFLite Model
File: step3_test_tflite.py
Loads .tflite model
Runs dummy input
Prints prediction output

Run:
python step3_test_tflite.py

🔹 PART C – Project 2
Edge AI on Raspberry Pi (Simulation)
Since Raspberry Pi hardware was not available, execution was simulated on PC using TensorFlow Lite runtime.

🎯 Objective
Run TensorFlow Lite model locally simulating Raspberry Pi environment.

⚙️ Task 1 – Install TensorFlow Lite Runtime

On Raspberry Pi (Linux):

sudo apt update
pip install tflite-runtime

On PC (Simulation):
pip install tensorflow

🧠 Task 2 – Load TFLite Model

File: raspberry_pi_simulation.py

interpreter = tf.lite.Interpreter(model_path="mobilenet_model.tflite")
interpreter.allocate_tensors()

🔍 Task 3 – Run Inference

Two options:

Option A – Dummy Input (Used)
input_data = np.random.random(input_shape).astype(np.float32)

Option B – Camera Input (Optional)
Using OpenCV:
import cv2

📊 Task 4 – Capture and Display Output
Example Output:
Inference successful!
Predicted class index: 885
Confidence: 0.8913

⚡ Task 5 – Performance Comparison
Feature	PC	Raspberry Pi
CPU Power	High	Limited
RAM	8–32GB	2–8GB
Inference Speed	Fast	Slower
Use Case	Development	Edge Deployment

🔎 Explanation
PC has stronger CPU and more RAM.
Raspberry Pi runs models slower due to hardware limits.
TFLite is optimized for low-power devices.
Edge devices prioritize power efficiency over speed.

💻 Installation Guide

1️⃣ Clone Repository
git clone <your-repo-link>
cd Mobile_Edge_AI_Project

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

📦 Requirements
Python 3.10+
TensorFlow
NumPy
(Optional) OpenCV for camera input

🎓 Learning Outcomes
Understanding TensorFlow Lite conversion
Running inference on edge devices
Handling model deployment pipeline
Comparing cloud vs edge performance
Git version control management

🏁 Final Status
✔ Model converted successfully
✔ TFLite model executed successfully
✔ Inference output generated
✔ Raspberry Pi simulation completed
✔ Git repository prepared

👨‍💻 Author
Anushka Unhalkar

Outputs: (Screenshots)

![Img1](https://github.com/user-attachments/assets/26d72353-4d84-479e-9eea-ed4cd302212d)

![Img2](https://github.com/user-attachments/assets/b9ccca46-53a8-4f0e-9bd7-73f62accfd64)

![Img3](https://github.com/user-attachments/assets/f121db9e-031b-45ee-84d5-9b4c0802e508)

![Img4](https://github.com/user-attachments/assets/ec14a5d3-a85b-413b-aa06-23bea157722b)

![Img5](https://github.com/user-attachments/assets/2b7b6fe8-9ae1-4da1-8d68-3c7d2d506049)




