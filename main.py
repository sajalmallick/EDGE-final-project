from fastapi import FastAPI, UploadFile, File, Query
from fastapi.responses import JSONResponse
from model import train_model, predict_with_model
import os

app = FastAPI()

@app.post("/learn")
async def learn(file: UploadFile = File(...)):
    contents = await file.read()
    with open("uploaded_data.csv", "wb") as f:
        f.write(contents)
    try:
        train_model("uploaded_data.csv")
        return {"message": "Model trained successfully!"}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/ask")
def ask(q: str = Query(...)):
    try:
        prediction = predict_with_model(q)
        return {"prediction": prediction}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
