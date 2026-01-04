# batch_resize.py
# Usage: python batch_resize.py input_dir output_dir 800

import os
import sys
from PIL import Image

INPUT_DIR = sys.argv[1]
OUTPUT_DIR = sys.argv[2]
MAX_SIZE = int(sys.argv[3])  # e.g. 800

os.makedirs(OUTPUT_DIR, exist_ok=True)

EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp")

for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(EXTENSIONS):
        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename)

        with Image.open(input_path) as img:
            img.thumbnail((MAX_SIZE, MAX_SIZE))
            img.save(output_path)

print("Done resizing images.")
