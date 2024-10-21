from ..time.day import Day
from ..time.time import Time

class TimeService:
    @classmethod
    def create(cls):
        # Implementation details here
        pass

    @classmethod
    def destroy(cls):
        # Implementation details here
        pass

    # testing purpose(intentionally added for setters)
    @classmethod
    def set_minute(cls, minute):
        cls.the_minute = minute

    @classmethod
    def set_day(cls, day):
        cls.the_day = day

    # testing purpose(intentionally added for getters)
    @classmethod
    def get_minute(cls):
        return cls.the_minute

    @classmethod
    def get_day(cls):
        return cls.the_day

    @classmethod
    def get_time(cls):
        return Time(cls.the_minute, cls.the_day)

    @classmethod
    def matches_now(cls, reaction_day, minute):
        if cls.get_minute() != minute:
            return False

        today = cls.get_day()
        if reaction_day == Day.EVERYDAY.get_value():
            return True
        if reaction_day == today:
            return True
        if reaction_day == Day.WEEKEND.get_value() and (today == Day.SATURDAY.get_value() or today == Day.SUNDAY.get_value()):
            return True
        if reaction_day == Day.WEEKDAY.get_value() and Day.MONDAY.get_value() <= today <= Day.FRIDAY.get_value():
            return True

        return False

