import requests
from PIL import Image
import json
import base64
from io import BytesIO


#import test image as a Pillow image from the images folder
IMG_FILE = './images/sunfloweroil.jpg'
img = Image.open(IMG_FILE)

#Convert Pillow Image to bytes 
buffered = BytesIO()
img.save(buffered, format="JPEG")
img_byte = buffered.getvalue()
# convert to base64 (still bytes at this point)
img_base64 = base64.b64encode(img_byte)

#convert bytes to str so it can be sent with json
img_str = img_base64.decode('utf-8') 

# prepare data to be sent with json
files = {
    "text":"test_image",
    "img":img_str
    }

r = requests.post("http://127.0.0.1:5000/test", json=json.dumps(files)) #POST to server as json

print(r.json())