# **Decoding Scriptures of Indus Valley Civilization**  
This project aims to decode and understand the ancient Harappan (Indus Valley Civilization) scripts using **Natural Language Processing (NLP)** and **data processing techniques**. The primary goal is to analyze symbols and texts to reconstruct potential meanings or linguistic patterns from these historical artifacts.  

---

## **Project Overview**  
The **Indus Valley Civilization**, one of the earliest civilizations in history, left behind a vast collection of undeciphered symbols. This project employs **NLP techniques** and **image processing** to:  
- **Preprocess** the data.  
- **Classify** the images.  
- **Analyze** symbols to identify linguistic patterns that may aid in decoding the language.  

---

## **Creating the Dataset**  
In the first phase of the project, the following steps were undertaken:  
1. **Processed 135 core seals**, categorizing them into:  
   - Entire Image  
   - Textual Image  
   - Symbolic Image  
2. For missing categories, the absent ones were initialized as `0` for consistency.  
3. Converted all images to **Base64 strings** for storage in CSV format.  
4. Processed an external file containing **time, location, and description** of the seals:  
   - Converted the file to CSV format.  
   - Dropped irrelevant columns.  
   - Merged the processed file with the image data.  

### **Outputs**  
- A consolidated **DataFrame**.  
- A **ZIP file** of categorized images.  
- A **final CSV file** containing all processed data.  

---

### **Text and Symbol Extraction**
OCR Challenges: Initial attempts using OCR (Tesseract) for text extraction highlighted difficulties in recognizing ancient scripts.
Contour-based Extraction: A custom contour-detection algorithm was developed to accurately extract individual symbols and textual elements.

---

### **Clustering and Symbol Analysis**

Feature Extraction:
Utilized Histograms of Oriented Gradients (HOG) to extract key visual features of the symbols.

Clustering Techniques:
Applied KMeans Clustering to group similar symbols based on extracted features.
Used Principal Component Analysis (PCA) for dimensionality reduction, enhancing clustering efficiency.

Cluster Organization:
Symbols were organized into directories corresponding to clusters for structured analysis and storage.

---

### **Comparison with Other Ancient Scripts**
Compared extracted symbols with scripts like Grantha and Kharosthi using cosine similarity.
Identified potential linguistic similarities and patterns to aid in the deciphering of the Indus script.

---

### **Outputs**

Data and Metadata:
A consolidated DataFrame combining images and metadata.
A ZIP file containing categorized seal images for organized storage.
A final CSV file with all processed data.

Clustering Results:
Directories of symbols organized by clusters.
Analyzed clusters with visualizations of symbol groupings.

Script Comparison Results:
Analysis Report summarizing similarities between the Indus script and other ancient scripts.

---

### **Conclusion**
This project provides a structured methodology to analyze and decode the Indus Valley Civilization's script using modern computational techniques. While the script remains undeciphered, the insights gained from clustering, comparisons, and symbol analysis bring us closer to understanding the language and culture of this ancient civilization.
