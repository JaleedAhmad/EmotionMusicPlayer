from tensorflow.keras.models import load_model

# Load without compiling
model = load_model("emotion_model.h5", compile=False)

# Display model summary
model.summary()
