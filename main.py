from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.responses import JSONResponse

import database
from database import engine, Base
from models import *
from crud import *
# from paddleocr import PaddleOCR
import numpy as np
import cv2

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI()
# ocr = PaddleOCR(lang='korean')

Base.metadata.create_all(bind=engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    logger.info("root")
    return {"Hello": "World1"}

@app.post("/api/ocr/plate")
async def read_item(image: UploadFile = File(...), db: Session = Depends(get_db)):
# async def read_item(image: UploadFile = File(...)):
    logger.info("/api/ocr/plate")
    try:
        # 이미지 로드
        file_data = await image.read()
        nparr = np.frombuffer(file_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img is None:
            return JSONResponse(status_code=400, content={"message": "이미지 디코딩 실패"})

        license_plate_text = '12가3457'
        # result = ocr.ocr(img, det=False, cls=False)
        #
        # if result:  # 결과가 비어있지 않다면
        #     lines = result[0]  # 첫 번째 OCR 결과만 사용
        #     for line in lines:
        #         license_plate_text = line[0]
        #         print(license_plate_text)
        # else:
        #     print("OCR 결과 없음")

        db_lp = get_license_plate(db, license_plate_text)
        if db_lp is None:
            create_license_plate(db, license_plate_text)

        return {"message": "OK", "license_plate_text": license_plate_text}

    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})