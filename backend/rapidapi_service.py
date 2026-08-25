import os
import requests
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

RAPIDAPI_HOST = "irctc1.p.rapidapi.com"


def get_live_train_status(train_no: str, start_day: int = 1):

    url = "https://irctc1.p.rapidapi.com/api/v1/liveTrainStatus"

    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST
    }

    params = {
        "trainNo": train_no,
        "startDay": start_day
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    response.raise_for_status()

    result = response.json()

    data = result.get("data", {})

    return {
        "status": result.get("status"),
        "message": result.get("message"),
        "train_number": data.get("train_number"),
        "train_name": data.get("train_name"),
        "is_run_day": data.get("is_run_day"),
        "destination_code": data.get("destination"),
        "destination_station": data.get("dest_stn_name"),
        "current_station_code": data.get("current_station_code"),
        "current_station": data.get("current_station_name"),
        "train_status": data.get("status"),
        "update_time": data.get("update_time"),
        "distance_from_source": data.get("distance_from_source"),
        "total_distance": data.get("total_distance")
    }