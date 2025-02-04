from predict import PredictionPipeline

# Replace this with an actual image path from your dataset or test images
image_path = "/Users/samarthtikotkar/Downloads/test_the_model/IM-0129-0001.jpeg"  # Example: "sample_images/test1.jpeg"

# Create an instance of PredictionPipeline
pipeline = PredictionPipeline(image_path)

# Run the prediction
result = pipeline.predict()

# Print the result
print("Prediction Result:", result)
