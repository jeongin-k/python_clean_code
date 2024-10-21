from enum import Enum

class TimeConstants(Enum):
    MINUTE_UNKNOWN = -1
    DAY_UNKNOWN = -1

    def get_value(self):
        return self.value

