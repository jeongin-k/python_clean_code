from .x10_house_code import X10HouseCode
from .light_id import LightId
from .light_state import LightState
from ..light_controller import LightController

class LightDriver():

    @classmethod
    def reset(cls):
        cls.states = [LightState.UNKNOWN.value] * LightController.MAX_LIGHTS
        cls.last_id = LightId.UNKNOWN.value
        cls.last_state = LightState.UNKNOWN.value

    @classmethod
    def add_spies_to_controller(cls, controller):
        for i in range(LightController.MAX_LIGHTS):
            spy = cls(i)
            controller.add(i, spy)

    @classmethod
    def update(cls, id, state):
        cls.states[id] = state
        cls.last_id = id
        cls.last_state = state

    @classmethod
    def get_state(cls, id):
        if 0 <= id < LightController.MAX_LIGHTS:
            return cls.states[id]
        return LightState.UNKNOWN.value

    @classmethod
    def get_last_id(cls):
        return cls.last_id

    @classmethod
    def get_last_state(cls):
        return cls.last_state

    def __init__(self, id):
        self._id = id
        self._type = "SPY"

    def x10_create(self):
        self._type = "LED"
        self._id = id
        self.unit = unit
        self.message = message
        self.house = house

    def x10_turn_on(self):
        # Implement LED light turning on logic
        pass

    def x10_turn_off(self):
        # Implement LED light turning off logic
        pass

    def x10_destroy(self):
        # Implement LED light destruction logic
        pass

    def memory_mapped_create(self):
        self._type = "Memory mapped"
        self._id = id
        self.addresses = addresses if addresses is not None else []

    def memory_mapped_turn_on(self):
        # Implement LED light turning on logic
        pass

    def memory_mapped_turn_off(self):
        # Implement LED light turning off logic
        pass

    def memory_mapped_destroy(self):
        # Implement LED light destruction logic
        pass

    def acme_wireless_create(self):
        self._type = "Acme wireless"
        self._id = id
        self.ssid = ssid
        self.key = key
        self.channel = channel

    def acme_wireless_turn_on(self):
        # Implement LED light turning on logic
        pass

    def acme_wireless_turn_off(self):
        # Implement LED light turning off logic
        pass

    def acme_wireless_destroy(self):
        # Implement LED light destruction logic
        pass

    def spy_turn_on(self):
        self.update(self._id, LightState.ON.value)

    def spy_turn_off(self):
        self.update(self._id, LightState.OFF.value)

    def spy_destroy(self):
        # No specific actions required for destruction in Python (GC)
        pass

    def get_type(self):
        return self._type

    def get_id(self):
        return self._id
