from typing import Union
from fastapi import FastAPI
from fastapi import FastAPI, UploadFile, Form, File
from fastapi.responses import JSONResponse
import numpy as np
import cv2

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/ocr/plate")
async def read_item(image: UploadFile = File(...)):
    try:
        # 이미지 로드
        file_data = await image.read()
        nparr = np.frombuffer(file_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img is None:
            return JSONResponse(status_code=400, content={"message": "이미지 디코딩 실패"})

        return {"message": "성공"}

    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})