import csv


# Convert HH:MM into minutes
def time_to_minutes(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute


# Read train data from CSV
def load_trains(filename):
    trains = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            trains.append(row)

    return trains


# Simulate the impact of a maintenance block
def simulate_impact(trains, block_track, block_start, block_end):

    block_start_minutes = time_to_minutes(block_start)
    block_end_minutes = time_to_minutes(block_end)

    affected_trains = []
    affected_passengers = 0

    for train in trains:

        # Ignore trains using another track
        if train["track_id"] != block_track:
            continue

        train_start = time_to_minutes(train["start_time"])
        train_end = time_to_minutes(train["end_time"])

        # Check if train overlaps with maintenance block
        if train_start < block_end_minutes and train_end > block_start_minutes:

            affected_trains.append(train["train_id"])
            affected_passengers += int(train["passengers"])

    return {
        "track_id": block_track,
        "block_start": block_start,
        "block_end": block_end,
        "affected_trains": affected_trains,
        "affected_train_count": len(affected_trains),
        "affected_passengers": affected_passengers
    }


# Load the team's train data
trains = load_trains("data/train_movements.csv")


# Example maintenance block
result = simulate_impact(
    trains,
    "S003",
    "01:00",
    "03:00"
)


# Display result
print("===== TRACKSENSE SIMULATION =====")
print("Blocked Track:", result["track_id"])
print("Maintenance Time:",
      result["block_start"], "-", result["block_end"])

print("\nAffected Trains:")

for train_id in result["affected_trains"]:
    print("-", train_id)

print("\nTotal Affected Trains:",
      result["affected_train_count"])

print("Total Affected Passengers:",
      result["affected_passengers"])