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