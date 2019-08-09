# Dated 08/08/2019
# Author - Hamood
# Import necessary modules
import cv2
import os
path = '/MyWork/PYTHON/OpenCV'
image_file = "ImageTransformation/FirstImage.jpg"
# Update directory to current working folder if not the same
try:
    os.chdir(path)
    if os.path.exists(image_file) == True and os.path.isfile(image_file) == True:
        image = cv2.imread(image_file) # cv2 module reads the image and stores it in n-dimensional array
        # We can use other way to store image directly as gray scale => cv2.imread(image, 0)
        # We can convert to many different color types. BGR2GRAY is used as cv2 stores image data in
        # BGR instead of RGB format which is the standard color pattern.
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert colored image to gray scale image
        # Display both colored and grayscale image. The first parameter is the window name second one is image
        cv2.imshow("COLORED", image)
        cv2.imshow("GrayScale", img)
        # The image displayed will be available on screen as long as a keystroke action is used. 0 indicates
        # time in milliseconds the process will wait before taking keystroke action as input.
        cv2.waitKey(0)
    else:
        print("Check file path and name")
except FileNotFoundError as e:
    print("Not a directory", e)
finally:
    cv2.destroyAllWindows()
