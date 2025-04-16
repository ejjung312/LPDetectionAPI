from fastapi import FastAPI, UploadFile, Form, File
from fastapi.responses import JSONResponse
from paddleocr import PaddleOCR
import numpy as np
import cv2

app = FastAPI()
ocr = PaddleOCR(lang='korean')

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

        result = ocr.ocr(img, det=False, cls=False)

        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                print(line[0])

        return {"message": "성공"}

    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})