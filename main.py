from recognition import FaceRecognition
# pip install cmake dlib==19.22
from typing import Union

from fastapi import FastAPI

if __name__ == '__main__':
    fr = FaceRecognition()
app = FastAPI()

@app.get("/facerecognition")
def face_recog():
    fr = FaceRecognition()
    # fr.run_recognition() x    
    return { fr.run_recognition()}
