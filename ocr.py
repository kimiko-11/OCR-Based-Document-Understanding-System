import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_with_boxes(image):
    data = pytesseract.image_to_data(
        image,
        output_type=pytesseract.Output.DICT
    )
    return data


def draw_boxes(image, data):
    img_copy = image.copy()

    for i in range(len(data['text'])):
        text = data['text'][i].strip()
        conf = int(data['conf'][i])

        if text != "" and conf > 60:
            x = data['left'][i]
            y = data['top'][i]
            w = data['width'][i]
            h = data['height'][i]

            # Draw rectangle
            cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Put text label (optional but nice)
            cv2.putText(img_copy, text, (x, y - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    return img_copy