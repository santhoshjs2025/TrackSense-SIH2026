from fastapi import FastAPI
from pydantic import BaseModel
from backend.data_loader import (
    get_maintenance_blocks,
    get_track_risk,
    get_train_movements
)

app = FastAPI(title="TrackSense API")


class BlockRequest(BaseModel):
    section: str
    maintenance_type: str
    duration_hours: float
    priority: str
    preferred_date: str
    expected_trains: int


@app.get("/")
def home():
    return {
        "message": "TrackSense backend is running!",
        "status": "success"
    }


@app.post("/plan-block")
def plan_block(request: BlockRequest):
    return {
        "message": "Maintenance request received successfully",
        "request": request
    }
@app.get("/maintenance-blocks")
def maintenance_blocks():
    return get_maintenance_blocks().to_dict(orient="records")


@app.get("/track-risk")
def track_risk():
    return get_track_risk().to_dict(orient="records")


@app.get("/train-movements")
def train_movements():
    return get_train_movements().to_dict(orient="records")