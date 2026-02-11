import tensorflow as tf

# Load SavedModel
converter = tf.lite.TFLiteConverter.from_saved_model("mobilenet_saved_model")

# Optional optimization (recommended for edge)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# Convert to TFLite
tflite_model = converter.convert()

# Save TFLite model
with open("mobilenet_model.tflite", "wb") as f:
    f.write(tflite_model)

print("Model converted to TFLite successfully!")
