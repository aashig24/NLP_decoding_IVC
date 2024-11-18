*Decoding Scriptures of Indus Valley Civilization*
This project aims to decode and understand the ancient Harappan (Indus Valley Civilization) scripts using NLP and data processing techniques. The primary objective is to identify and analyze symbols and texts to reconstruct potential meanings or linguistic patterns from these artifacts.

*Project Overview*
The Indus Valley Civilization, one of the earliest civilizations in history, left behind a large collection of symbols that remain largely undeciphered. This project leverages Natural Language Processing (NLP) techniques and image processing to preprocess, classify, and analyze these symbols, in hopes of uncovering linguistic patterns that may help decode the language.

*Creating Dataset*
In the first phase of our project, we processed 135 core seals, categorizing them into entire image, textual image, and symbolic image. For seals missing categories, we initialized the absent ones as 0. To handle image data in a CSV format, all images were converted to Base64 strings. Additionally, we processed an external file containing the time, location, and description of the seals, converting it to CSV, dropping irrelevant columns, and merging it with the image data. The outputs include a consolidated DataFrame, a ZIP file of categorized images, and a final CSV file.
