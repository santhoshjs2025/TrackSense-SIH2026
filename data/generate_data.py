import pandas as pd
import random

# Make the results reproducible
random.seed(42)

data = []

# Generate 100 synthetic railway track records
for i in range(1, 101):

    track_id = f"S{i:03d}"

    # Track information
    condition_score = random.randint(20, 95)
    defects = random.randint(0, 10)
    failures = random.randint(0, 5)
    days_since_inspection = random.randint(5, 60)
    traffic_density = random.randint(20, 100)
    track_age = random.randint(2, 40)

    # Maintenance information
    maintenance_duration = random.randint(1, 6)

    # Convert different factors into risk values
    condition_risk = 100 - condition_score
    defect_risk = defects * 10
    failure_risk = failures * 20
    inspection_risk = (days_since_inspection / 60) * 100
    traffic_risk = traffic_density
    age_risk = (track_age / 40) * 100

    # Calculate prototype risk score
    risk_score = (
        0.30 * condition_risk +
        0.20 * defect_risk +
        0.15 * failure_risk +
        0.10 * inspection_risk +
        0.15 * traffic_risk +
        0.10 * age_risk
    )

    # Convert score into risk category
    if risk_score >= 75:
        risk_level = "CRITICAL"
    elif risk_score >= 55:
        risk_level = "HIGH"
    elif risk_score >= 35:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    data.append([
        track_id,
        condition_score,
        defects,
        failures,
        days_since_inspection,
        traffic_density,
        track_age,
        maintenance_duration,
        risk_score,
        risk_level
    ])


# Column names
columns = [
    "track_id",
    "condition_score",
    "defects",
    "failures",
    "days_since_inspection",
    "traffic_density",
    "track_age",
    "maintenance_duration",
    "risk_score",
    "risk_level"
]

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save CSV
df.to_csv("data/track_risk_data.csv", index=False)

print("Dataset created successfully!")
print()
print(df.head(20))

print("\nRisk distribution:")
print(df["risk_level"].value_counts())
import os
print("Python is running from:", os.getcwd())
