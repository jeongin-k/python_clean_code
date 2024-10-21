from .day import Day
from .month import Month

class Time:
    def __init__(self, minute_of_day, day_of_week):
        self.usec = 0
        self.sec = 0
        self.minute_of_day = minute_of_day
        self.minute_of_hour = 0
        self.day_of_week = day_of_week
        self.day_of_month = 0
        self.month = None

    def matches_day_of_week(self, day):
        today = self.day_of_week

        if day == Day.EVERYDAY:
            return True
        if day == Day.WEEKEND and (today == Day.SATURDAY.value or today == Day.SUNDAY.value):
            return True
        if day == Day.WEEKDAY and Day.MONDAY.value <= today <= Day.FRIDAY.value:
            return True
        return day.value == today

    def matches_minute_of_day(self, minute):
        return self.minute_of_day == minute

