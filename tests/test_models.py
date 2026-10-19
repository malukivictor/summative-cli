from datetime import date, timedelta
from models import DailyHabit, WeeklyHabit


def test_mark_done_adds_a_check_in():
    habit = DailyHabit("Read")
    assert habit.mark_done() is True
    assert len(habit.get_check_ins()) == 1


def test_cannot_check_in_twice_in_one_day():
    habit = DailyHabit("Read")
    habit.mark_done()
    assert habit.mark_done() is False


def test_daily_streak_counts_consecutive_days():
    today = date.today()
    days = [str(today), str(today - timedelta(days=1)), str(today - timedelta(days=2))]
    habit = DailyHabit("Read", days)
    assert habit.streak() == 3


def test_daily_streak_breaks_after_a_missed_day():
    today = date.today()
    habit = DailyHabit("Read", [str(today), str(today - timedelta(days=2))])
    assert habit.streak() == 1


def test_weekly_streak_counts_this_week():
    habit = WeeklyHabit("Exercise", [str(date.today())])
    assert habit.streak() == 1