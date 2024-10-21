from ..devices.light_driver import LightDriver
from ..devices.light_id import LightId
from ..devices.light_state import LightState
from ..light_controller import LightController

class SpyLightDriver(LightDriver):
    type = "SPY"
    states = [LightState.UNKNOWN.value] * LightController.MAX_LIGHTS
    last_id = LightId.UNKNOWN.value
    last_state = LightState.UNKNOWN.value

    def __init__(self, id):
        self.id = id

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

    def destroy(self):
        # No specific actions required for destruction in Python (GC)
        pass

    def turn_on(self):
        self.update(self.id, LightState.ON.value)

    def turn_off(self):
        self.update(self.id, LightState.OFF.value)

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

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

