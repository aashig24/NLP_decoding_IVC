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
