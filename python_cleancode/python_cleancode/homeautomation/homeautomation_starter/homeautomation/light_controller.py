
class LightController:
    MAX_LIGHTS = 100  # Adjust as needed

    def __init__(self):
        self.light_drivers = [None] * self.MAX_LIGHTS

    def create(self):
        self.light_drivers = [None] * self.MAX_LIGHTS

    def destroy_driver(self, driver):
        driver_type = driver.get_type()
        if driver_type == "LED":
            driver.x10_destroy()
        elif driver_type == "memory mapped":
            driver.memory_mapped_destroy()
        elif driver_type == "Acme wireless":
            driver.acme_wireless_destroy()
        elif driver_type == "SPY":
            driver.spy_destroy()

    def destroy(self):
        for driver in self.light_drivers:
            if driver is not None:
                self.destroy_driver(driver)

    def is_id_in_bounds(self, id):
        return id < 0 or id >= self.MAX_LIGHTS

    def add(self, id, light_driver):
        if self.is_id_in_bounds(id) or light_driver is None:
            return False

        if self.light_drivers[id] is not None:
            self.destroy_driver(self.light_drivers[id])

        self.light_drivers[id] = light_driver
        return True

    def remove(self, id):
        if self.is_id_in_bounds(id) or self.light_drivers[id] is None:
            return False

        self.destroy_driver(self.light_drivers[id])
        self.light_drivers[id] = None
        return True

    def turn_on(self, id):
        if self.is_id_in_bounds(id) or self.light_drivers[id] is None:
            return
        driver_type = self.light_drivers[id].get_type()
        if driver_type == "LED":
            self.light_drivers[id].x10_turn_on()
        elif driver_type == "memory mapped":
            self.light_drivers[id].memory_mapped_turn_on()
        elif driver_type == "Acme wireless":
            self.light_drivers[id].acme_wireless_turn_on()
        elif driver_type == "SPY":
            self.light_drivers[id].spy_turn_on()

    def turn_off(self, id):
        if self.is_id_in_bounds(id) or self.light_drivers[id] is None:
            return
        driver_type = self.light_drivers[id].get_type()
        if driver_type == "LED":
            self.light_drivers[id].x10_turn_off()
        elif driver_type == "memory mapped":
            self.light_drivers[id].memory_mapped_turn_off()
        elif driver_type == "Acme wireless":
            self.light_drivers[id].acme_wireless_turn_off()
        elif driver_type == "SPY":
            self.light_drivers[id].spy_turn_off()

