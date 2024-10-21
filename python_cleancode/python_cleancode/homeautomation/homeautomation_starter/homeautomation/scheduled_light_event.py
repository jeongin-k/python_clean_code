from enum import Enum
from random import randint

from .light_control_event import LightControlEvent


class Day(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class RandomMinute:
    def get(self):
        return randint(0, 59)


class ScheduledLightEvent:
    UNUSED = -1

    def __init__(self, id, day, minute, event, randomize):
        self.id = id
        self.day = day
        self.minute_of_day = minute
        self.event = event
        self.randomize = randomize
        self.random_minute = RandomMinute()
        self.random_minutes = 0
        self.reset_randomize()

    def is_in_use(self):
        return self.id != self.UNUSED

    def match_event(self, id, day, minute):
        return self.id == id and self.day == day and self.minute_of_day == minute

    def reset_randomize(self):
        if self.randomize == LightControlEvent.RANDOM_ON.value:
            self.random_minutes = self.random_minute.get()
        else:
            self.random_minutes = 0

