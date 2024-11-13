import base64
import pandas as pd
from io import BytesIO
import zipfile
import re

# Function to encode image to base64 from binary data
def image_to_base64(image_data):
    return base64.b64encode(image_data).decode('utf-8')

# Load the ZIP file and extract images
zip_path = "/content/Indus-Seal-Dataset-master.zip"

# Dictionary to hold the processed data
csv_data = []

# Open the ZIP file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    # Get all file names in the ZIP archive
    file_list = sorted(zip_ref.namelist())

    # Create a dictionary to store images for each symbol ID
    image_dict = {}

    # Loop through each file path in the zip
    for file in file_list:
        # Use regex to match files inside subdirectories like "1/1.jpg", "10/10symbolic.jpg"
        match = re.match(r"Indus-Seal-Dataset-master/(\d+)/(\d+)(.*)\.(jpg|jpeg|png)$", file)
        if match:
            symbol_id = int(match.group(1))  # Folder name (symbol ID)
            image_type = match.group(3).lower()  # Determine the type based on suffix

            if symbol_id not in image_dict:
                image_dict[symbol_id] = {"Symbol_ID": symbol_id}

            # Determine the type of image and add to the dictionary
            try:
                image_data = zip_ref.read(file)
                if image_type == "":
                    image_dict[symbol_id]["Image_Base64"] = image_to_base64(image_data)
                elif "symbolic" in image_type:
                    image_dict[symbol_id]["Symbolic_Image_Base64"] = image_to_base64(image_data)
                elif "text" in image_type:
                    image_dict[symbol_id]["Text_Image_Base64"] = image_to_base64(image_data)
            except KeyError:
                # Skip if the file is not found (in case of some error)
                pass

    # Prepare the final CSV data
    for idx, (symbol_id, images) in enumerate(image_dict.items(), start=1):
        csv_data.append({
            "Image No": idx,  # Adding the consecutive number
            "Symbol_ID": images.get("Symbol_ID"),
            "Image_Base64": images.get("Image_Base64", image_to_base64(b'\x00' * 100)),
            "Symbolic_Image_Base64": images.get("Symbolic_Image_Base64", image_to_base64(b'\x00' * 100)),
            "Text_Image_Base64": images.get("Text_Image_Base64", image_to_base64(b'\x00' * 100)),
        })

# Convert to DataFrame and save to CSV
df = pd.DataFrame(csv_data)
df.to_csv("/content/Base_64.csv", index=False)

# Confirm the file generation
df.head()
