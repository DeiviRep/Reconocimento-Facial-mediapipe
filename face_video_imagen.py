import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def get_face_prueba():
    with mp_face_mesh.FaceMesh(
        static_image_mode=True,
        max_num_faces=1,
        min_detection_confidence=0.5) as face_mesh:

        while True:
            ret, frame = cap.read()
            if ret == False:
                break
            frame = cv2.flip(frame, 1)

            cv2.imshow("Frame", frame)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

            # Convierte el frame a formato RGB para que MediaPipe lo pueda procesar
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Procesa el frame con la solución FaceMesh de MediaPipe
            results = face_mesh.process(frame_rgb)

            # Dibuja la malla facial en el frame
            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    mp_drawing.draw_landmarks(
                        frame,
                        face_landmarks,
                        mp_face_mesh.FACEMESH_TESSELATION,
                        landmark_drawing_spec=None,
                        connection_drawing_spec=mp_drawing.DrawingSpec(
                            color=(0, 255, 0), thickness=1, circle_radius=1))

            # Convierte el frame de nuevo a formato BGR para que OpenCV lo pueda mostrar
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            # Codifica el frame en formato JPEG y lo convierte en una cadena de bytes
            _, buffer = cv2.imencode('.jpg', frame)
            jpeg_str = buffer.tobytes()

            # Devuelve la cadena de bytes como una respuesta HTTP
            return jpeg_str

    cap.release()
    cv2.destroyAllWindows()
