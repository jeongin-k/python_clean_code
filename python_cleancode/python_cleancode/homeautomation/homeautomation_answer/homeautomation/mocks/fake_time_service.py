from ..devices.time_service import TimeService
from ..time.time import Time
from .time_constants import TimeConstants

class FakeTimeService(TimeService):
    def __init__(self):
        self.the_minute = TimeConstants.MINUTE_UNKNOWN.get_value()
        self.the_day = TimeConstants.DAY_UNKNOWN.get_value()

    def set_minute(self, minute):
        self.the_minute = minute

    def set_day(self, day):
        self.the_day = day

    def get_minute(self):
        return self.the_minute

    def get_day(self):
        return self.the_day

    def get_time(self):
        return Time(self.the_minute, self.the_day)

