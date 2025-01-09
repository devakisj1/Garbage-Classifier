import os
import cv2
from random import randint
from scipy.ndimage import zoom

def augment_image(image_path, output_folder):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to read image '{image_path}'")
        return

    # Generate augmented images
    flipped_image = cv2.flip(image, 1)
    zoom_factor = 1 + randint(-50, 50) / 100.0
    zoomed_image = zoom(flipped_image, zoom=(zoom_factor, zoom_factor, 1))
    rotated_image = cv2.rotate(zoomed_image, cv2.ROTATE_180)
    aug_image = cv2.resize(rotated_image, (image.shape[1], image.shape[0]))

    filename = os.path.splitext(os.path.basename(image_path))[0]
    # Save augmented images
    cv2.imwrite(os.path.join(output_folder, f"{filename}_aug.jpg"), aug_image)

if __name__ == "__main__":
    # Input image path and output folder
    input_folder= ""
    output_folder = "output_folder"

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            input_image_path = os.path.join(input_folder, filename)
            # Call the augmentation function for each image
            augment_image(input_image_path, output_folder)
