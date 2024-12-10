import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load pre-trained VGG16 model (without the classification head)
def load_model():
    model = VGG16(weights="imagenet", include_top=False, pooling="avg")
    return model

# Preprocess input images
def preprocess_image(image_path, target_size=(224, 224)):
    img = load_img(image_path, target_size=target_size)
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

# Extract features using VGG16
def extract_features(model, image_path):
    processed_image = preprocess_image(image_path)
    features = model.predict(processed_image)
    return features

# Compute cosine similarity
def compute_similarity(features1, features2):
    similarity = cosine_similarity(features1, features2)
    return similarity[0][0]

# Main function
def main(grantha_image_path, indus_image_path):
    print("Loading model...")
    model = load_model()
    
    print("Extracting features...")
    grantha_features = extract_features(model, grantha_image_path)
    indus_features = extract_features(model, indus_image_path)
    
    print("Computing similarity...")
    similarity_score = compute_similarity(grantha_features, indus_features)
    
    print(f"Similarity between Grantha and Indus script: {similarity_score:.4f}")

# Example usage
if __name__ == "__main__":
    grantha_image_path = "/content/granthadata.jpg"  # Replace with the actual path
    indus_image_path = "/content/indusdata.jpg"      # Replace with the actual path
    main(grantha_image_path, indus_image_path)
