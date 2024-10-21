from enum import Enum

class LightState(Enum):
    UNKNOWN = -1
    OFF = 0
    ON = 1

    def get_value(self):
        return self.value

