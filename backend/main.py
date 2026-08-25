from fastapi import FastAPI
from pydantic import BaseModel
from backend.data_loader import (
    get_maintenance_blocks,
    get_maintenance_blocks_by_track,
    get_track_risk,
    get_train_movements,
    get_track_risk_by_id,
    get_train_movements_by_track
)
from backend.rapidapi_service import get_live_train_status
app = FastAPI(title="TrackSense API")


class BlockRequest(BaseModel):
    section: str
    maintenance_type: str
    duration_hours: float
    priority: str
    preferred_date: str
    expected_trains: int
    train_number: str | None = None

@app.get("/")
def home():
    return {
        "message": "TrackSense backend is running!",
        "status": "success"
    }
@app.get("/live-train-status")
def live_train_status(train_no: str, start_day: int = 1):

    return get_live_train_status(train_no, start_day)

@app.post("/plan-block")
def plan_block(request: BlockRequest):

    track_data = get_track_risk_by_id(request.section)
    train_data = get_train_movements_by_track(request.section)
    block_data = get_maintenance_blocks_by_track(request.section)
    live_train_data = None

    if request.train_number:
        try:
            live_train_data = get_live_train_status(
                request.train_number,
                1
            )
        except Exception as e:
            live_train_data = {
                "error": "Unable to fetch live train status",
                "details": str(e)
            }
    if track_data.empty:
        return {
            "message": "Track not found",
            "section": request.section
        }

    return {
    "message": "Maintenance request received successfully",
    "request": request,
    "track_risk": track_data.to_dict(orient="records"),
    "train_movements": train_data.to_dict(orient="records"),
    "existing_blocks": block_data.to_dict(orient="records"),
    "live_train_status": live_train_data
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