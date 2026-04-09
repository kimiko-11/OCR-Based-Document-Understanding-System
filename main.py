from preprocessing import preprocess_image
from ocr import extract_text_optimized, extract_with_boxes, draw_boxes
import cv2

results = preprocess_image(r"C:\Users\Kimaya\doc_scanner\archive (5)\SROIE2019\train\img\X00016469612.jpg")

# OCR
text = extract_text_optimized(results["deskewed"])
print(text)

# Bounding boxes
data = extract_with_boxes(results["deskewed"])
boxed_img = draw_boxes(results["original"], data)

cv2.imshow("Detected Text", boxed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

from preprocessing import preprocess_image
from ocr import extract_text_optimized
from extract import extract_all

results = preprocess_image(r"C:\Users\Kimaya\doc_scanner\archive (5)\SROIE2019\train\img\X00016469612.jpg")

text = extract_text_optimized(results["deskewed"])
print("RAW TEXT:\n", text)

data = extract_all(text)
print("\nSTRUCTURED OUTPUT:\n", data)