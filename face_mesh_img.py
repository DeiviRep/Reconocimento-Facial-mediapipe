from typing import Union
import cv2
import time
import mediapipe as mp
from fastapi import FastAPI

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

def get_face_mesh_img():
    with mp_face_mesh.FaceMesh(
        static_image_mode=True,
        max_num_faces=1,
        min_detection_confidence=0.5) as face_mesh:
        
        image = cv2.imread("./rostro.jpg")
        height, width, _ = image.shape
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image_rgb)
    
        print("Face landmarcks: ", results.multi_face_landmarks)
        if results.multi_face_landmarks is not  None:
            for face_landmarks in results.multi_face_landmarks:
                # x = int(face_landmarks.landmark[4].x * width)
                # y = int(face_landmarks.landmark[4].y * height)
                mp_drawing.draw_landmarks(
                    image, face_landmarks, mp_face_mesh.FACEMESH_CONTOURS,
                    mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=1, circle_radius=1),
                    mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=1, circle_radius=1)
                )
    
        cv2.imshow("Image",image)
        cv2.waitKey(1 * 1000) 
        cv2.destroyAllWindows()
        return results
