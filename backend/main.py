from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

# Import your own math engine!
from engine import fit_linear, fit_polynomial

app = FastAPI()

# --- 1. Define the Data Format ---
# This tells the server: "I expect a list of numbers for X and Y"
class DataRequest(BaseModel):
    x: List[float]
    y: List[float]
    degree: int = 1  # Default to 1 (Linear)

@app.get("/")
def read_root():
    return {"message": "CurveGen API is active. Go to /docs to test it."}

# --- 2. The Curve Fitting Endpoint ---
# This is the "Door" the website will knock on.
@app.post("/fit")
def fit_curve(data: DataRequest):
    # Check if user wants linear or polynomial
    if data.degree == 1:
        result = fit_linear(data.x, data.y)
    else:
        result = fit_polynomial(data.x, data.y, data.degree)
    
    return result

# --- 3. Run the Server (only if run directly) ---
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)