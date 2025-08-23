import cv2
import requests
import sys, os
import json

def resource_path(relative_path):
    #Get absolute path to resource (works for dev and for PyInstaller)
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

vid=cv2.VideoCapture(0)

# Load configuration from JSON file
try:
    with open("config.json", 'r') as config_file:
        config = json.load(config_file)
        FACESET_TOKEN = config["FACESET_TOKEN"]
        API_KEY = config["API_KEY"]
        API_SECRET = config["API_SECRET"]
except:
    print("u havnt made the config.json file")

try:
    with open("Faces.json",'r') as f1:
        d=json.load(f1)
except:
    with open("Faces.json",'w') as f1:
        json.dump("{}",f1)
    with open("Faces.json",'r') as f1:
        d=json.load(f1)
        
print("press r to run")

while True:
    
    #u see urself 
    ret, frame=vid.read()
    if not ret:
        break
    cv2.imshow("camera",frame)
    cv2.moveWindow("camera", 1920 - 640 - 387, 0)
    
    if cv2.waitKey(1) & 0xFF == ord('r'):
        
        #face detection
        face_cascade = cv2.CascadeClassifier(resource_path("Haar_Face_detector.xml"))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        if len(faces) > 0:
            print("face detected")
            ret, jpeg = cv2.imencode('.jpg', frame)
            files = {'image_file': ('image.jpg', jpeg.tobytes(), 'image/jpeg')}

            try:
                #face encoding
                response = requests.post("https://api-us.faceplusplus.com/facepp/v3/detect", data={
                    'api_key': API_KEY,
                    'api_secret': API_SECRET,
                }, files=files)
                if 'faces' in response.json() and response.json()['faces']:
                    face_token = response.json()['faces'][0]['face_token']
                    # Search in FaceSet 
                    search_res = requests.post("https://api-us.faceplusplus.com/facepp/v3/search", data={
                        'api_key': API_KEY,
                        'api_secret': API_SECRET,
                        'face_token': face_token,
                        'faceset_token': FACESET_TOKEN,
                    })
                    search_json = search_res.json()

                    # If matched user found
                    if 'results' in search_json and search_json['results'][0]['confidence'] > 80:
                        matched_token = search_json['results'][0]['face_token']
                        Flag=True
                        for name, saved_token in d.items():
                            if saved_token == matched_token:
                                print(f"Welcome, {name}")
                                Flag=False
                                break
                        if Flag:
                            print("ur face is recognised but ur name in not saved locally")
                            name = input("Enter your name: ")
                            d[name] = matched_token
                            
                            with open("Faces.txt", 'w') as f:
                                f.write(str(d))
                            
                            
                        break
                    
                    # If matched user not found
                    else:
                        ch = input("New face. Create account? (y/n): ")
                        if ch.lower() == 'y':
                            name = input("Enter your name: ")
                            d[name] = face_token

                            # Save locally
                            with open("Faces.json", 'w') as f1:
                                json.dump("{d",f1)

                            # Add to FaceSet
                            requests.post("https://api-us.faceplusplus.com/facepp/v3/faceset/addface", data={
                                'api_key': API_KEY,
                                'api_secret': API_SECRET,
                                'faceset_token': FACESET_TOKEN,
                                'face_tokens': face_token
                            })
                            print("Account created.")
                            break
            except:
                print("Error in face encoding. Please check ur internet connection.")
                continue         


vid.release()
cv2.destroyAllWindows()

input("Press Enter to close")
