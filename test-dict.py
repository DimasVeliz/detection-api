cams = [
        {
            "id_cam": 2,
            "path_cam":0,
            "type": "cam_outside",
            "model":"x"
        },
        {
            "id_cam": 1,
            "path_cam":1,
            "type": "cam_outside",
            "model":"x"
        },
        {
            "id_cam": 0,
            "path_cam":2,
"type": "cam_door",
                        "model":"x"
        }
    ]


payloads = []
for cam in cams: 
    
    payloads.append(cam)
    
        
print(payloads)
        
