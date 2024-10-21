
class LightController:
    MAX_LIGHTS = 100  # Adjust as needed

    def __init__(self):
        self.light_drivers = [None] * self.MAX_LIGHTS

    def create(self):
        self.light_drivers = [None] * self.MAX_LIGHTS

    def destroy(self):
        for driver in self.light_drivers:
            if driver is not None:
                driver.destroy()

    def is_id_in_bounds(self, id):
        return id < 0 or id >= self.MAX_LIGHTS

    def add(self, id, light_driver):
        if self.is_id_in_bounds(id) or light_driver is None:
            return False

        if self.light_drivers[id] is not None:
            self.light_drivers[id].destroy()

        self.light_drivers[id] = light_driver
        return True

    def remove(self, id):
        if self.is_id_in_bounds(id) or self.light_drivers[id] is None:
            return False

        self.light_drivers[id].destroy()
        self.light_drivers[id] = None
        return True

    def turn_on(self, id):
        if self.is_id_in_bounds(id) or self.light_drivers[id] is None:
            return
        self.light_drivers[id].turn_on()

    def turn_off(self, id):
        if self.is_id_in_bounds(id) or self.light_drivers[id] is None:
            return
        self.light_drivers[id].turn_off()

