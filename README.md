# Detection-api:

This repository features a web api that can be queried to obtain the objects identified within an image frame.

## Methods:
```
POST REQUEST:

import requests

url = 'http://localhost:5001/clasify?access_token=ACCESS_TOKEN&type=TYPE'
files = {'media': open('test.jpg', 'rb')}
requests.post(url, files=files)



SERVER RESPONSE:
    [
        {
            class:"person"
            x:10
            y:20
            heigth:50
            width:20
        },
        {
            class:"dog"
            x:1
            y:4
            heigth:5
            width:10
        },

    ]
```