from ..time.day import Day
from ..time.time import Time

class TimeService:
    def create(self):
        # Implementation details here
        pass

    def destroy(self):
        # Implementation details here
        pass

    def get_minute(self):
        # Implementation details here
        return 0

    def get_day(self):
        # Implementation details here
        return 0

    def get_time(self):
        # Implementation details here
        return None

    def matches_now(self, reaction_day, minute):
        if self.get_minute() != minute:
            return False

        today = self.get_day()
        if reaction_day == Day.EVERYDAY.get_value():
            return True
        if reaction_day == today:
            return True
        if reaction_day == Day.WEEKEND.get_value() and (today == Day.SATURDAY.get_value() or today == Day.SUNDAY.get_value()):
            return True
        if reaction_day == Day.WEEKDAY.get_value() and Day.MONDAY.get_value() <= today <= Day.FRIDAY.get_value():
            return True

        return False

