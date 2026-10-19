# Habit Tracker CLI

A command-line app for building good routines. Add habits, check them off when you do them, and see your streak (how many days or weeks in a row). Data is saved in a JSON file, so your habits are still there next time.

## Features
- Add daily or weekly habits
- Check in once per day per habit
- View streaks and list all habits
- Data saved automatically in `data.json`

## Project Structure
- `main.py`: CLI commands (argparse)
- `models.py`: `Habit`, `DailyHabit`, `WeeklyHabit` (inheritance and encapsulation)
- `storage.py`: saving and loading JSON
- `tests/`: unit tests

## Installation
1. git clone https://github.com/malukivictor/summative-cli.git
2. cd summative-cli
3. pipenv install

Requires Python 3.10+ and pipenv.

## Usage
Run with `pipenv run python main.py` followed by a command:

| Command | What it does |
|---|---|
| add-habit NAME | Add a daily habit (use `--weekly` for weekly) |
| list-habits | Show all habits and streaks |
| check-in NAME | Mark a habit as done today |
| streak NAME | Show a habit's streak |

Use quotes for names with spaces, for example `add-habit "Drink water"`.
For help, run `pipenv run python main.py --help`.

## Tests
pipenv run python -m pytest

## Team
- Monicah
- Victor