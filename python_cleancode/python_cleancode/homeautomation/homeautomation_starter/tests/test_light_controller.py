import unittest
from homeautomation.light_controller import LightController
from homeautomation.devices.light_state import LightState
from homeautomation.devices.light_driver import LightDriver

class LightControllerTest(unittest.TestCase):
    def setUp(self):
        self.light_controller = LightController()
        LightDriver.add_spies_to_controller(self.light_controller)
        LightDriver.reset()

    def tearDown(self):
        self.light_controller.destroy()

    def test_create_destroy(self):
        # No specific actions required
        pass

    def test_driver_is_destroyed_by_light_controller(self):
        spy = LightDriver(1)
        self.light_controller.add(1, spy)

    def test_turn_on(self):
        self.light_controller.turn_on(7)
        self.assertEqual(LightState.ON.value, LightDriver.get_state(7))

    def test_turn_off(self):
        self.light_controller.turn_off(1)
        self.assertEqual(LightState.OFF.value, LightDriver.get_state(1))

    def test_all_drivers_destroyed(self):
        for i in range(LightController.MAX_LIGHTS):
            spy = LightDriver(i)
            self.assertTrue(self.light_controller.add(i, spy))

    def test_valid_id_lower_range(self):
        spy = LightDriver(0)
        self.assertTrue(self.light_controller.add(0, spy))

    def test_valid_id_upper_range(self):
        spy = LightDriver(LightController.MAX_LIGHTS - 1)
        self.assertTrue(self.light_controller.add(LightController.MAX_LIGHTS - 1, spy))

    def test_invalid_id_beyond_upper_range(self):
        spy = LightDriver(LightController.MAX_LIGHTS)
        self.assertFalse(self.light_controller.add(LightController.MAX_LIGHTS, spy))

    def test_remove_existing_light_driver_succeeds(self):
        self.assertTrue(self.light_controller.remove(10))

    def test_removed_light_does_nothing(self):
        self.light_controller.remove(1)
        self.light_controller.turn_on(1)
        self.assertEqual(LightState.UNKNOWN.value, LightDriver.get_state(1))
        self.light_controller.turn_off(1)
        self.assertEqual(LightState.UNKNOWN.value, LightDriver.get_state(1))

    def test_rejects_null_drivers(self):
        self.assertFalse(self.light_controller.add(1, None))

    def test_remove_non_existing_light_driver_fails(self):
        self.assertTrue(self.light_controller.remove(10))
        self.assertFalse(self.light_controller.remove(10))

if __name__ == '__main__':
    unittest.main()

