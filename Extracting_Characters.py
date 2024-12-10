import cv2

# Generate a list of image paths dynamically
image_paths = [f"/content/{i}text.jpg" for i in range(1, 21)]  # From 1text.jpg to 134text.jpg

# Define minimum width and height for a contour to be considered a symbol
min_width = 10   # Adjust as needed
min_height = 10  # Adjust as needed

# Loop through each image path
for image_path in image_paths:
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Image not found or could not be loaded: {image_path}")
        continue  # Skip to the next image

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Otsu's thresholding to create a binary image
    _, binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # List to hold extracted symbols
    symbols = []

    # Loop through contours and filter by size
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        #print(f"Image {image_path} - Contour found with width: {w} and height: {h}")  # Debug output
        if w > min_width and h > min_height:  # Filter out small contours
            symbol = binary_image[y:y+h, x:x+w]
            symbols.append(symbol)

    # Check if any symbols were found
    if symbols:
        # Resize and save/display each segmented symbol
        for i, symbol in enumerate(symbols):
            resized_symbol = cv2.resize(symbol, (32, 32))
            output_path = f"symbol_{i}_{image_path.split('/')[-1]}"  # Unique filename for each symbol
            cv2.imwrite(output_path, resized_symbol)  # Saves each symbol as a separate file
        print(f"{len(symbols)} symbols saved for image {image_path}.")
    else:
        print(f"No symbols found in image {image_path} with the current settings.")
