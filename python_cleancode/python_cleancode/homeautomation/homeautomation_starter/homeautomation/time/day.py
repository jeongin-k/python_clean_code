from enum import Enum

class Day(Enum):
    EVERYDAY = -3
    WEEKDAY = -2
    WEEKEND = -1
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7

    def get_value(self):
        return self.value

