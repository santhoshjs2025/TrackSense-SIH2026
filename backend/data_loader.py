import pandas as pd
from pathlib import Path


# Find the main project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Location of the dataset folder
DATA_DIR = BASE_DIR / "data"


# Load railway datasets
maintenance_blocks = pd.read_csv(
    DATA_DIR / "maintenance_blocks.csv"
)

track_risk = pd.read_csv(
    DATA_DIR / "track_risk_data.csv"
)

train_movements = pd.read_csv(
    DATA_DIR / "train_movements.csv"
)


def get_maintenance_blocks():
    return maintenance_blocks


def get_track_risk():
    return track_risk


def get_train_movements():
    return train_movements

def get_track_risk_by_id(track_id):
    result = track_risk[track_risk["track_id"] == track_id]
    return result

def get_train_movements_by_track(track_id):
    result = train_movements[train_movements["track_id"] == track_id]
    return result

def get_maintenance_blocks_by_track(track_id):
    result = maintenance_blocks[maintenance_blocks["track_id"] == track_id]
    return result