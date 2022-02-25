import base64
import json
from flask import Flask, jsonify, request
from io import BytesIO
from PIL import Image
import os 


app = Flask(__name__)

@app.route("/receive_img", methods=["GET", "POST"])
def receive_img():
    json_data = request.get_json() #Get the json from the POST request
    

    payload = json.loads(json_data) #Convert json to dictionary
    if payload ["status"] == True: # check the status before parsing the dict data
        dict_data = payload["files"]
        img = dict_data["img"] #Take out base64 str
        img = base64.b64decode(img) 
        img = BytesIO(img) 
        img = Image.open(img)


        # Dynamically create folders based on which camera the image is from

        # check to see if directory exists, and if it doesn't, create one:
        if not os.path.exists(os.path.join('.', f'cam{dict_data["id_cam"]}')):
            os.makedirs(os.path.join('.', f'cam{dict_data["id_cam"]}'))
        # if directory for the camera already exists, save img to that folder: 
        else:
            img.save(os.path.join('.', f'cam{dict_data["id_cam"]}', 'img.jpg'))
    
        # process the rest of the files from payload
        text = dict_data["text"] 
        id_cam = dict_data["id_cam"]
        cam_type = dict_data["type"]
        model = dict_data["model"]

        #Return the processing result to the client
        response = {
            "text": text,
            "id_cam": id_cam,
            "type": cam_type,
            "model": model,
            "message": f'Image received from Camera {id_cam}'     
            }

        return jsonify(response)


if __name__ == "__main__":
    app.debug = True
    app.run()