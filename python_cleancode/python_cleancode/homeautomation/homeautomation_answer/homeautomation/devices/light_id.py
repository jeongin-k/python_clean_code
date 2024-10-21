from enum import Enum

class LightId(Enum):
    UNKNOWN = -1

    def get_value(self):
        return self.value

