from .light_driver import LightDriver
from .x10_house_code import X10HouseCode

class X10LightDriver(LightDriver):
    def __init__(self, id, unit=0, message="", house=X10HouseCode.X10_A):
        self._type = "LED"
        self._id = id
        self.unit = unit
        self.message = message
        self.house = house

    def turn_on(self):
        # Implement LED light turning on logic
        pass

    def turn_off(self):
        # Implement LED light turning off logic
        pass

    def destroy(self):
        # Implement LED light destruction logic
        pass

    def get_type(self):
        return self._type

    def get_id(self):
        return self._id

