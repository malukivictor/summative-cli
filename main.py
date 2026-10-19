import argparse
from models import DailyHabit, WeeklyHabit
from storage import load_habits, save_habits

NAME_HELP = "Name of the habit"

def find_habit(habits, name):
    for habit in habits:
        if habit.name.lower() == name.lower():
            return habit
    return None

parser = argparse.ArgumentParser(description="Habit Tracker")
commands = parser.add_subparsers(dest="command")

add = commands.add_parser("add-habit", help="Add a new habit")
add.add_argument("name", help=NAME_HELP)
add.add_argument("--weekly", action="store_true", help="Make it a weekly habit")

commands.add_parser("list-habits", help="Show all habits")

check = commands.add_parser("check-in", help="Mark a habit as done today")
check.add_argument("name", help="Name of the habit")

streak = commands.add_parser("streak", help="Show the streak of a habit")
streak.add_argument("name", help="Name of the habit")

args = parser.parse_args()
habits = load_habits()

if args.command == "add-habit":
    if find_habit(habits, args.name):
        print("That habit already exists.")
    else:
        habits.append(WeeklyHabit(args.name) if args.weekly else DailyHabit(args.name))
        save_habits(habits)
        print("Added:", args.name)

elif args.command == "list-habits":
    if not habits:
        print("No habits yet.")
    for h in habits:
        print(f"- {h.name} ({h.kind}), streak: {h.streak()}")

elif args.command == "check-in":
    habit = find_habit(habits, args.name)
    if habit is None:
        print("Habit not found.")
    elif habit.mark_done():
        save_habits(habits)
        print("Checked in:", habit.name)
    else:
        print("Already checked in today.")

elif args.command == "streak":
    habit = find_habit(habits, args.name)
    print(f"{habit.name}: {habit.streak()}" if habit else "Habit not found.")

else:
    parser.print_help()