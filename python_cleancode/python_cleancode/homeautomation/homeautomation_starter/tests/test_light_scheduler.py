import unittest
from homeautomation.light_controller import LightController
from homeautomation.light_scheduler import LightScheduler
from homeautomation.devices.light_state import LightState
from homeautomation.devices.time_service import TimeService
from homeautomation.devices.light_driver import LightDriver
from homeautomation.time.day import Day
from homeautomation.devices.light_id import LightId

class LightSchedulerTest(unittest.TestCase):
    def setUp(self):
        self.light_controller = LightController()
        self.time_service = TimeService()
        self.light_scheduler = LightScheduler(self.light_controller)
        self.scheduled_minute = 1234
        self.light_number = 4

        LightDriver.reset()
        self.light_controller.create()
        LightDriver.add_spies_to_controller(self.light_controller)
        self.light_scheduler.create()

    def tearDown(self):
        self.light_scheduler.destroy()
        self.light_controller.destroy()

    def check_light_state(self, id, level):
        if id == LightId.UNKNOWN.value:
            self.assertEqual(LightState.UNKNOWN.value, LightDriver.get_last_state())
        else:
            self.assertEqual(level.value, LightDriver.get_state(id))

    def set_time_to(self, day, minute):
        self.time_service.set_day(day.value)
        self.time_service.set_minute(minute)

    def test_create_does_not_change_the_lights(self):
        self.assertEqual(LightId.UNKNOWN.value, LightDriver.get_last_id())
        self.assertEqual(LightState.UNKNOWN.value, LightDriver.get_last_state())

    def test_schedule_everyday_not_time_yet(self):
        self.light_scheduler.schedule_turn_on(3, Day.EVERYDAY, self.scheduled_minute)
        self.set_time_to(Day.MONDAY, self.scheduled_minute - 1)
        self.light_scheduler.wake_up()
        self.check_light_state(LightId.UNKNOWN.value, LightState.UNKNOWN)

    def test_schedule_on_today_its_time(self):
        self.light_scheduler.schedule_turn_on(3, Day.EVERYDAY, self.scheduled_minute)
        self.set_time_to(Day.MONDAY, self.scheduled_minute)
        self.light_scheduler.wake_up()
        self.check_light_state(3, LightState.ON)

    def test_schedule_on_tuesday_and_its_not_tuesday_and_its_time(self):
        self.light_scheduler.schedule_turn_on(3, Day.TUESDAY, self.scheduled_minute)
        self.set_time_to(Day.MONDAY, self.scheduled_minute)
        self.light_scheduler.wake_up()
        self.check_light_state(LightId.UNKNOWN.value, LightState.UNKNOWN)

    def test_schedule_on_tuesday_and_its_tuesday_and_its_time(self):
        self.light_scheduler.schedule_turn_on(3, Day.TUESDAY, self.scheduled_minute)
        self.set_time_to(Day.TUESDAY, self.scheduled_minute)
        self.light_scheduler.wake_up()
        self.check_light_state(3, LightState.ON)

    def test_schedule_off_tuesday_and_its_tuesday_and_its_time(self):
        self.light_scheduler.schedule_turn_off(self.light_number, Day.TUESDAY, self.scheduled_minute)
        self.set_time_to(Day.TUESDAY, self.scheduled_minute)
        self.light_scheduler.wake_up()
        self.check_light_state(self.light_number, LightState.OFF)

    def test_schedule_off_weekend_and_its_saturday_and_its_time(self):
        self.light_scheduler.schedule_turn_off(self.light_number, Day.WEEKEND, self.scheduled_minute)
        self.set_time_to(Day.SATURDAY, self.scheduled_minute)
        self.light_scheduler.wake_up()
        self.check_light_state(self.light_number, LightState.OFF)

    def test_schedule_on_weekend_and_its_sunday_and_its_time(self):
        self.light_scheduler.schedule_turn_on(self.light_number, Day.WEEKEND, self.scheduled_minute)
        self.set_time_to(Day.SUNDAY, self.scheduled_minute)
        self.light_scheduler.wake_up()
        self.check_light_state(self.light_number, LightState.ON)

    def test_schedule_on_weekend_and_its_monday_and_its_time(self):
        self.light_scheduler.schedule_turn_off(self.light_number, Day.WEEKEND, self.scheduled_minute)
        self.set_time_to(Day.MONDAY, self.scheduled_minute)
        self.check_light_state(LightId.UNKNOWN.value, LightState.UNKNOWN)

    def test_schedule_on_weekday_and_its_sunday_and_its_time(self):
        self.light_scheduler.schedule_turn_on(self.light_number, Day.WEEKEND, self.scheduled_minute)
        self.set_time_to(Day.SUNDAY, self.scheduled_minute)
        self.light_scheduler.wake_up()
        self.check_light_state(self.light_number, LightState.ON)

    def test_schedule_on_weekday_and_its_monday_and_its_time(self):
        self.light_scheduler.schedule_turn_on(self.light_number, Day.WEEKDAY, self.scheduled_minute)
        self.set_time_to(Day.MONDAY, self.scheduled_minute)
        self.light_scheduler.wake_up()
        self.check_light_state(self.light_number, LightState.ON)

    def test_schedule_on_weekday_and_its_friday_and_its_time(self):
        self.light_scheduler.schedule_turn_on(self.light_number, Day.WEEKDAY, self.scheduled_minute)
        self.set_time_to(Day.FRIDAY, self.scheduled_minute)
        self.light_scheduler.wake_up()
        self.check_light_state(self.light_number, LightState.ON)

    def test_schedule_on_weekday_and_its_saturday_and_its_time(self):
        self.light_scheduler.schedule_turn_on(self.light_number, Day.WEEKDAY, self.scheduled_minute)
        self.set_time_to(Day.SATURDAY, self.scheduled_minute)
        self.light_scheduler.wake_up()
        self.check_light_state(LightId.UNKNOWN.value, LightState.UNKNOWN)

    def test_remove_scheduled_event(self):
        self.light_scheduler.schedule_turn_on(6, Day.MONDAY, self.scheduled_minute)
        self.light_scheduler.schedule_remove(6, Day.MONDAY, self.scheduled_minute)
        self.set_time_to(Day.MONDAY, self.scheduled_minute)
        self.light_scheduler.wake_up()
        self.check_light_state(LightId.UNKNOWN.value, LightState.UNKNOWN)

    def test_multiple_scheduled_events_same_time(self):
        self.light_scheduler.schedule_turn_off(4, Day.MONDAY, self.scheduled_minute)
        self.light_scheduler.schedule_turn_on(3, Day.MONDAY, self.scheduled_minute)

        self.set_time_to(Day.MONDAY, self.scheduled_minute)
        self.light_scheduler.wake_up()

        self.check_light_state(4, LightState.OFF)
        self.check_light_state(3, LightState.ON)

    def test_multiple_scheduled_events_different_times(self):
        self.light_scheduler.schedule_turn_off(4, Day.MONDAY, self.scheduled_minute)
        self.light_scheduler.schedule_turn_on(3, Day.MONDAY, self.scheduled_minute + 1)

        self.set_time_to(Day.MONDAY, self.scheduled_minute)
        self.light_scheduler.wake_up()

        self.check_light_state(4, LightState.OFF)

        self.set_time_to(Day.MONDAY, self.scheduled_minute + 1)
        self.light_scheduler.wake_up()

        self.check_light_state(3, LightState.ON)

if __name__ == '__main__':
    unittest.main()

