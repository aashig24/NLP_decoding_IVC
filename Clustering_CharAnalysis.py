import zipfile
import numpy as np
from skimage.feature import hog
from skimage.color import rgb2gray
from skimage.io import imread
from PIL import Image
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import io
import os

# Path to the uploaded zip file
zip_file_path = "/content/symbols1.zip"

# Step 1: Load and preprocess images from ZIP
def load_images_from_zip(zip_path, target_size=(64, 64)):
    images = []
    filenames = []
    with zipfile.ZipFile(zip_path, 'r') as z:
        for file_name in z.namelist():
            if file_name.endswith(('.png', '.jpg')):
                with z.open(file_name) as f:
                    image = imread(io.BytesIO(f.read()))  # Read image
                    # Check if the image has an alpha channel
                    if image.shape[-1] == 4:
                        # If yes, remove the alpha channel by slicing
                        image = image[:, :, :3]
                    gray_image = rgb2gray(image)  # Convert to grayscale
                    resized_image = np.array(Image.fromarray(gray_image).resize(target_size))
                    images.append(resized_image)
                    filenames.append(file_name)
    return np.array(images), filenames

# Step 2: Extract Features using HOG
def extract_hog_features(images):
    hog_features = []
    for image in images:
        features = hog(image, pixels_per_cell=(8, 8), cells_per_block=(2, 2), feature_vector=True)
        hog_features.append(features)
    return np.array(hog_features)

# Step 3: Perform Clustering
def cluster_symbols(features, n_clusters=5):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(features)
    return labels, kmeans.cluster_centers_

# Step 4: Visualize Clusters
def visualize_clusters(images, labels, filenames, n_clusters=5):
    plt.figure(figsize=(15, 10))
    for cluster_id in range(n_clusters):
        cluster_indices = np.where(labels == cluster_id)[0]
        for i, idx in enumerate(cluster_indices[:5]):  # Display up to 5 symbols per cluster
            plt.subplot(n_clusters, 5, cluster_id * 5 + i + 1)
            plt.imshow(images[idx], cmap='gray')
            plt.axis('off')
            plt.title(f"Cluster {cluster_id+1}")
    plt.tight_layout()
    plt.show()

# Execution
images, filenames = load_images_from_zip(zip_file_path)
hog_features = extract_hog_features(images)
labels, _ = cluster_symbols(hog_features, n_clusters=5)
visualize_clusters(images, labels, filenames, n_clusters=5)






import os
from shutil import copyfile
from pathlib import Path

# Create output directories for each cluster
def save_clusters_to_directories(images, labels, filenames, output_dir="/content/data/clustered_symbols"):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    cluster_dirs = []
    for cluster_id in np.unique(labels):
        cluster_dir = os.path.join(output_dir, f"Cluster_{cluster_id}")
        os.makedirs(cluster_dir, exist_ok=True)
        cluster_dirs.append(cluster_dir)

        # Save images in their respective cluster directories
        cluster_indices = np.where(labels == cluster_id)[0]
        for idx in cluster_indices:
            image_path = os.path.join(cluster_dir, os.path.basename(filenames[idx]))
            img = Image.fromarray((images[idx] * 255).astype('uint8'))  # Convert normalized image back to uint8
            img.save(image_path)

    return cluster_dirs

# Generate a summary report
def generate_cluster_summary(labels):
    unique_clusters, counts = np.unique(labels, return_counts=True)
    print("\nCluster Summary:")
    for cluster_id, count in zip(unique_clusters, counts):
        print(f"Cluster {cluster_id}: {count} symbols")
    return dict(zip(unique_clusters, counts))

# Execution: Save and summarize
output_dir = "/content/data/clustered_symbols"
cluster_dirs = save_clusters_to_directories(images, labels, filenames, output_dir)
cluster_summary = generate_cluster_summary(labels)

print(f"\nClustered symbols saved in: {output_dir}")



import numpy as np
from skimage.io import imsave
import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Step 1: Generate a representative image for each cluster
def generate_representative_images(images, labels, output_dir="/content/data/representative_images"):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    unique_clusters = np.unique(labels)
    for cluster_id in unique_clusters:
        cluster_indices = np.where(labels == cluster_id)[0]
        cluster_images = images[cluster_indices]
        # Calculate the mean image for the cluster
        mean_image = np.mean(cluster_images, axis=0)
        # Optional: Smooth the image for better visualization
        smoothed_image = gaussian_filter(mean_image, sigma=1)

        # Convert the smoothed image to uint8 before saving
        smoothed_image = (smoothed_image * 255).astype(np.uint8)  # Convert to 0-255 range and uint8 type

        # Save the representative image
        imsave(os.path.join(output_dir, f"Cluster_{cluster_id}_representative.png"), smoothed_image)
    print(f"Representative images saved to {output_dir}")

# Step 2: Frequency analysis of symbols
def analyze_symbol_frequencies(labels):
    unique_clusters, counts = np.unique(labels, return_counts=True)
    freq_data = pd.DataFrame({"Cluster": unique_clusters, "Frequency": counts})
    print("\nFrequency of symbols by cluster:")
    print(freq_data)
    # Visualize frequencies
    plt.bar(freq_data["Cluster"], freq_data["Frequency"], color='skyblue')
    plt.title("Frequency of Symbols by Cluster")
    plt.xlabel("Cluster")
    plt.ylabel("Frequency")
    plt.show()
    return freq_data

# Step 3: Save the labeled dataset
def save_labeled_dataset(filenames, labels, output_file="/content/data/labeled_symbols.csv"):
    labeled_data = pd.DataFrame({"Filename": filenames, "Cluster": labels})
    labeled_data.to_csv(output_file, index=False)
    print(f"Labeled dataset saved to {output_file}")

# Execution
representative_output_dir = "/content/data/representative_images"
generate_representative_images(images, labels, representative_output_dir)
freq_data = analyze_symbol_frequencies(labels)
save_labeled_dataset(filenames, labels)
