# Import the necessary libraries
import cv2, os

# Load the image

file_path = os.path.abspath("assets/images/cats/water_tribe")
thumb_path = os.path.join(file_path, "thumbs")

if not os.path.exists( thumb_path ):
    os.mkdir(thumb_path)

# Define the scale factor
scale_factor = 0.1

for img in os.listdir(file_path):

    if img[-4:] != ".jpg":
        continue

    image = cv2.imread(os.path.join(file_path, img))
    
    # Get the original image dimensions
    height, width = image.shape[:2]

    # Calculate the new image dimensions
    new_height = int(height * scale_factor)
    new_width = int(width * scale_factor)

    # Scaled image
    scaled_image = cv2.resize(src= image, 
                            dsize =(new_width, new_height), 
                            interpolation=cv2.INTER_AREA)

    cv2.imwrite(os.path.join(thumb_path, img), scaled_image)
