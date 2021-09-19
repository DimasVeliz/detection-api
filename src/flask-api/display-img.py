# open the image that was sent through the API endpoint

from PIL import Image

# retrieve image from the uploads folder
RECEIVED_IMG_FILE = './downloads/test.png'
img = Image.open(RECEIVED_IMG_FILE)

# open image to make sure it was sent successfully and the file is uncorrupted  
img.show()