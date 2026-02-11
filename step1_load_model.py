import tensorflow as tf

# Load pre-trained MobileNetV2
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Export as SavedModel (Required for TFLite)
model.export("mobilenet_saved_model")

print("Model exported successfully!")
