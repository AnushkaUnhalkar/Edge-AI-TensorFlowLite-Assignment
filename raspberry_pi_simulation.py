import numpy as np
import tensorflow as tf

print("Simulating Raspberry Pi TFLite Execution...")

# Load TFLite model
interpreter = tf.lite.Interpreter(model_path="mobilenet_model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Create dummy input
input_shape = input_details[0]['shape']
input_data = np.random.random_sample(input_shape).astype(np.float32)

# Run inference
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()

output_data = interpreter.get_tensor(output_details[0]['index'])

print("Inference successful!")
print("Predicted class index:", np.argmax(output_data))
print("Confidence:", float(np.max(output_data)))
