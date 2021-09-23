import cv2

key = cv2.waitKey(1)
webcam = cv2.VideoCapture(0)

while True: 

    try: 
        is_working, frame = webcam.read()
        cv2.imshow("Capturing image...", frame)
        key = cv2.waitKey(1)

        # use space key to capture an image
        if key == 32: 
            cv2.imwrite(filename='.\images\saved_img.jpg', img=frame)
            webcam.release()
            new_img = 'saved_img.jpg'
            cv2.imshow("Captured Image", new_img)
            # wait 2 seconds and then close windows
            cv2.waitKey(2)
            cv2.destroyAllWindows()

            break

        # use ESC key to quit program
        elif key == 27: 
            webcam.release()
            cv2.destroyAllWindows()
            break 

    except(KeyboardInterrupt):
        webcam.release()
        cv2.destroyAllWindows()
        break 