from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import shutil
import os
import pandas as pd
from classify import classify_from_csv

app = FastAPI()

@app.post("/classify")
async def classify_endpoint(file: UploadFile = File(...)):
    input_path = "resources/uploaded.csv"
    output_path = "resources/output.csv"

    # Save uploaded file
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Check required columns before classification
    try:
        df = pd.read_csv(input_path)
        required_columns = {"source", "log_message"}
        if not required_columns.issubset(df.columns):
            raise HTTPException(
                status_code=400,
                detail=f"CSV must contain columns: {', '.join(required_columns)}"
            )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error reading CSV file: {str(e)}"
        )

    # Call the classify function
    try:
        classify_from_csv(input_path)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error during classification: {str(e)}"
        )

    # Return the output file as response
    return FileResponse(
        output_path,
        media_type="text/csv",
        filename="output.csv"
    )