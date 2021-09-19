import base64
import json
from flask import Flask, jsonify, request
from io import BytesIO
from PIL import Image


app = Flask(__name__)

@app.route("/test", methods=["GET", "POST"])
def test():
    json_data = request.get_json() #Get the POSTed json
    dict_data = json.loads(json_data) #Convert json to dictionary

    img = dict_data["img"] #Take out base64# str
    img = base64.b64decode(img) #Convert image data converted to base64 to original binary data# bytes
    img = BytesIO(img) # _io.Converted to be handled by BytesIO pillow
    img = Image.open(img) 

    # image was being saved as a PNG instead of a JPG, but I am not sure why
    # save the image to the downloads folder, for future use
    img.save('./downloads/test.png')
    
    text = dict_data["text"] #Properly process with the acquired text

    #Return the processing result to the client
    response = {
        "text": text,
        "message": 'The image made it, yay!'     
        }

    return jsonify(response)

if __name__ == "__main__":
    app.debug = True
    app.run()