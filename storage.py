import json
from models import DailyHabit, WeeklyHabit

FILE = "data.json"


def save_habits(habits):
    try:
        with open(FILE, "w") as f:
            json.dump([h.to_dict() for h in habits], f, indent=2)
    except OSError as error:
        print("Could not save data:", error)


def load_habits():
    try:
        with open(FILE) as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("data.json is damaged, starting with an empty list.")
        return []

    habits = []
    for item in data:
        cls = WeeklyHabit if item["type"] == "weekly" else DailyHabit
        habits.append(cls(item["name"], item["check_ins"]))
    return habits