from .light_driver import LightDriver

class MemoryMappedLightDriver(LightDriver):
    def __init__(self, id, addresses=None):
        self._type = "Memory mapped"
        self._id = id
        self.addresses = addresses if addresses is not None else []

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

