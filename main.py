from rembg import remove
import cv2
# path of input image (my file: image.jpeg)
input_path = 'images/car10.png'
# path for saving output image and saving as a output.jpeg
output_path = 'images/car10_out.jpeg'
# Reading the input image
input = cv2.imread(input_path)
# Removing background
output = remove(input)
# Saving file 
cv2.imwrite(output_path, output)
