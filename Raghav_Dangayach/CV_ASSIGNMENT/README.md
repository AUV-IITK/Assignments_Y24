# 🖼️ Braille Art Converter

This project is a Python-based image-to-text converter that transforms `.jpg` images into Braille Art using raw image processing techniques with OpenCV and NumPy. The final output is saved as a `.txt` file made of Unicode Braille characters, ideal for creative text rendering of visual content.

---

## 📌 Project Overview

The Braille Art Converter breaks down images into simplified black-and-white pixel blocks and maps those to Unicode Braille characters. The process runs entirely in Python and is optimized to run smoothly in **Google Colab**, allowing for easy uploads and downloads without requiring local setup.

This project is a fun way to visually reimagine images through the lens of text-based art and also introduces basic image processing concepts like grayscale conversion, thresholding, resizing, and pattern mapping.

---

## ✨ Features

- 🔲 Converts `.jpg` images to grayscale and then binary format.
- 🔍 Resizes images to reduce complexity and improve text representation.
- 🧩 Breaks image into 2x3 blocks and maps each to a Braille character.
- 📄 Outputs clean `.txt` files with Braille-based image renderings.
- ⚙️ Adjustable scale factor for output size customization.
- ☁️ Built to work seamlessly with Google Colab (easy uploads/downloads).

---

## ⚙️ Requirements

Install the following Python packages before running the script:

```bash
pip install opencv-python numpy

🚀 How It Works

Load the Image
The program uses OpenCV to read a .jpg image file provided by the user.

Convert to Grayscale
The image is converted to a single-channel grayscale format to simplify processing and reduce complexity.

Resize
To ensure the output remains readable in text format, the image is resized based on a scale_factor. This keeps the generated Braille art compact and manageable.

Apply Thresholding
The grayscale image is transformed into a binary black-and-white image using a fixed threshold value of 128. Pixels darker than the threshold become black (filled), and lighter pixels become white (empty).

Braille Mapping
The binary image is scanned in blocks of 2×3 pixels (to match the 6-dot layout of Braille characters). The number of filled (black) pixels in each block is counted and mapped to a simplified Braille character.

Output to Text File
The Braille characters for each row are joined into lines, and the entire output is written to a .txt file using UTF-8 encoding. This file contains a textual representation of the original image using Braille Unicode characters.

⚠️ Important Notes

The current Braille character mapping is simplified — all blocks with any filled pixels are represented by a default Braille character (⠿). This can be improved later to follow true Unicode Braille dot patterns based on pixel positions.

For best results, use high-contrast images, such as black-and-white sketches, line drawings, or logos. These translate more clearly into Braille Art.

Avoid using detailed or colorful images, as they lose a lot of visual clarity when resized and converted to binary (black and white).

The script does not support automatic file format detection. Please ensure that your input file is a .jpg image.

