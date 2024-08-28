from pptxtopdf import convert
import os

input_dir = r".\data\input\pptx"
output_dir = r".\data\output\pdf"

os.makedirs(output_dir, exist_ok=True)

convert(input_dir, output_dir)