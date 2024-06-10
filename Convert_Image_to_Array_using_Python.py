from PIL import Image
import numpy as np

# Load the image
image_path = 'path_to_your_image.jpg'  # Replace with your image path
image = Image.open(image_path)

# Convert image to a NumPy array
image_array = np.array(image)

# Display the array shape and data type
print("Array shape:", image_array.shape)
print("Array data type:", image_array.dtype)

# Optionally, print the array (commented out if not needed)
# print(image_array)

