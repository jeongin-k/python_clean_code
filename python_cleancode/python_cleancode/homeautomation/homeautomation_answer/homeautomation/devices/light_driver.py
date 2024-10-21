from abc import ABC, abstractmethod

class LightDriver(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def destroy(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_id(self):
        pass
