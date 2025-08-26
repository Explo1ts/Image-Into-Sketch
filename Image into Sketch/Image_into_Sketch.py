import cv2
import os

def image_to_sketch(image_path, output_path="sketch.png"):
    # Check if file exists
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        return
    
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read the image file.")
        return

    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    invert = cv2.bitwise_not(grey_img)
    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    inverted_blur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_img, inverted_blur, scale=256.0)
    cv2.imwrite(output_path, sketch)
    print(f"Sketch saved as '{output_path}'")
    cv2.imshow("Original", image)
    cv2.imshow("Sketch", sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = input("Enter image name with extension: ").strip()
    image_to_sketch(image_path)