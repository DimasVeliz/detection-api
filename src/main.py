import cv2
import requests 
import json
import base64
import time
from io import BytesIO

def take_picture():
    # read in cams array from cfg
    with open(".\cfg.json", "r") as file: 
        data = file.read()
    cfg = json.loads(data)
    cams_array = cfg["cams"]

    sleep_frequency = cfg["sleep_frequency"] # get from cfg.json    

    for cam_info in cams_array:
        status = True # check if there is an picture taken 
        files = None 
        cam_path = cam_info["path_cam"]
        print(f'Taking picture from camera {cam_path}')

        cam = cv2.VideoCapture(cam_path) 

        ret, frame = cam.read()

        if ret: 
            print(f'picture taken from camera {cam_path}')
            img_arr = cv2.imencode('.jpg', frame)
            img_bytes = img_arr[1].tobytes()
                    
                    # convert to base64 (still bytes at this point)
            img_base64 = base64.b64encode(img_bytes)

                    #convert bytes to str so it can be sent with json
            img_str = img_base64.decode('utf-8') 

                    # prepare data to be sent with json
            
            files = {
                "text": "test_image",
                "id_cam": cam_info["id_cam"],
                "type": cam_info["type"],
                "model":cam_info["model"],
                "img": img_str}

            payload = {
                "status": status, 
                "files": files
            }
                        

            r = requests.post("http://127.0.0.1:5000/receive_img", json=json.dumps(payload)) #POST to server as json

            print(r.json())
                        
            time.sleep(sleep_frequency)

            cam.release()
            cv2.destroyAllWindows()
        
        else: 
            status = False
        

        payload = {
            "status": status,
            "files": files
        }
        r = requests.post("http://127.0.0.1:5000/receive_img", json=json.dumps(payload)) # post error message to server as json
        

take_picture()