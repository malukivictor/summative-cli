from datetime import date, timedelta


class Habit:
    kind = "habit"

    def __init__(self, name, check_ins=None):
        self.name = name
        self._check_ins = check_ins or []  # private list of "YYYY-MM-DD" dates

    def mark_done(self):
        today = str(date.today())
        if today in self._check_ins:
            return False  # already checked in today
        self._check_ins.append(today)
        return True

    def get_check_ins(self):
        return list(self._check_ins)

    def streak(self):
        return 0

    def to_dict(self):
        return {"type": self.kind, "name": self.name, "check_ins": self._check_ins}


class DailyHabit(Habit):
    kind = "daily"

    def streak(self):
        count = 0
        day = date.today()
        while str(day) in self._check_ins:
            count += 1
            day -= timedelta(days=1)
        return count


class WeeklyHabit(Habit):
    kind = "weekly"

    def streak(self):
        dates = [date.fromisoformat(d) for d in self._check_ins]
        start = date.today() - timedelta(days=date.today().weekday())
        count = 0
        while any(start <= d < start + timedelta(days=7) for d in dates):
            count += 1
            start -= timedelta(days=7)
        return count