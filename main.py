from fastapi import FastAPI, Response
from typing import Union
from face_mesh_video import get_face_mesh_frame
from face_mesh_img import get_face_mesh_img
from face_video_imagen  import get_face_prueba
app = FastAPI()

urlImagen = "http://127.0.0.1:8000/img"
urlVideo = "http://127.0.0.1:8000/video"
prueba = "http://127.0.0.1:8000/prueba"
home = "http://127.0.0.1:8000"
@app.get("/")
async def read_root():
    return {"Hello": "autenticacion facial", "por Imagen": urlImagen, "por video": urlVideo, "prueba": prueba }

@app.get("/img")
async def read_face_mesh():
    jpeg_str = get_face_mesh_img()
    return {"content":"jpeg_str", "media_type":"image/jpeg", "inicio": home}

@app.get("/video")
async def read_face_mesh():
    jpeg_str = get_face_mesh_frame()
    return {"content":jpeg_str, "media_type":"image/jpeg", "inicio": home}

@app.get("/prueba")
async def read_face_mesh():
    jpeg_str = get_face_prueba()
    print(jpeg_str)
    return {"content":jpeg_str, "media_type":"image/jpeg", "inicio": home}