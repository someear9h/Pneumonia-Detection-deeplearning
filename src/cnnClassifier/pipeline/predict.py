import numpy as np
from keras.models import load_model
from keras.preprocessing import image

import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load model artifacts/training/model.h5
        model_path = "/Users/samarthtikotkar/Downloads/CODING/Data Science/ML projects/Pneumonia-Detection-deeplearning/artifacts/training/model.h5"
        model = load_model(model_path)

        # Load and preprocess image
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image) / 255.0  # Normalize
        test_image = np.expand_dims(test_image, axis=0)

        # Get raw predictions
        result_raw = model.predict(test_image)
        print("Raw Model Output:", result_raw)  # Debugging

        # Get the predicted class index
        predicted_class = np.argmax(result_raw, axis=1)[0]
        print("Predicted Class Index:", predicted_class)  # Debugging

        # **Check Class Mapping**
        class_labels = {0: "NORMAL", 1: "PNEUMONIA"}  # Modify if needed
        prediction = class_labels[predicted_class]

        return [{"image": prediction}]

# Run prediction if script is executed directly  IM-0129-0001.jpeg
if __name__ == "__main__":
    test_image_path = os.path.join("test_samples", "IM-0129-0001.jpeg") # person2_bacteria_3.jpeg 

    if not os.path.exists(test_image_path):
        print(f"Error: Image '{test_image_path}' not found!")
    else:
        pipeline = PredictionPipeline(test_image_path)
        prediction = pipeline.predict()
        print("Prediction Result:", prediction)
