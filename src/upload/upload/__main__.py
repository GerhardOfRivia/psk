import uvicorn
from fastapi import FastAPI, File, UploadFile
import shutil
import os

app = FastAPI()

UPLOAD_DIRECTORY = "uploaded_files"

# Ensure upload directory exists
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "content_type": file.content_type}


@app.get("/")
def root():
    return {"message": "Welcome to FastAPI File Upload Service"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
