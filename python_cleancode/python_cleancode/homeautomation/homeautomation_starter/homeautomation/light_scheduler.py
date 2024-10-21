from .time.day import Day
from .time.time import Time
from .devices.time_service import TimeService
from .scheduled_light_event import ScheduledLightEvent
from .light_control_event import LightControlEvent

class LightScheduler:
    MAX_EVENTS = 100  # Adjust as needed

    def __init__(self, light_controller):
        self.time_service = TimeService()
        self.event_list = [ScheduledLightEvent(ScheduledLightEvent.UNUSED, Day.EVERYDAY, 0, LightControlEvent.TURN_OFF, 0) for _ in range(self.MAX_EVENTS)]
        self.light_controller = light_controller

    def create(self):
        for i in range(self.MAX_EVENTS):
            self.event_list[i] = ScheduledLightEvent(ScheduledLightEvent.UNUSED, Day.EVERYDAY, 0, LightControlEvent.TURN_OFF, 0)

    def destroy(self):
        # No specific actions required for destruction
        pass

    def find_unused_event(self):
        for event in self.event_list:
            if not event.is_in_use():
                return event
        return None

    def schedule_event(self, id, day, minute, event, randomize):
        scheduled_event = self.find_unused_event()
        if scheduled_event:
            scheduled_event.id = id
            scheduled_event.day = day
            scheduled_event.minute_of_day = minute
            scheduled_event.event = event
            scheduled_event.randomize = randomize
            scheduled_event.reset_randomize()

    def schedule_turn_on(self, id, day, minute):
        self.schedule_event(id, day, minute, LightControlEvent.TURN_ON, LightControlEvent.RANDOM_OFF.value)

    def schedule_turn_off(self, id, day, minute):
        self.schedule_event(id, day, minute, LightControlEvent.TURN_OFF, LightControlEvent.RANDOM_OFF.value)

    def randomize(self, id, day, minute):
        for event in self.event_list:
            if event.match_event(id, day, minute):
                event.randomize = LightControlEvent.RANDOM_ON.value
                event.reset_randomize()
                break

    def schedule_remove(self, id, day, minute):
        for event in self.event_list:
            if event.match_event(id, day, minute):
                event.id = ScheduledLightEvent.UNUSED
                break

    def operate_light(self, event):
        if event.event == LightControlEvent.TURN_ON:
            self.light_controller.turn_on(event.id)
        elif event.event == LightControlEvent.TURN_OFF:
            self.light_controller.turn_off(event.id)

    def wake_up(self):
        time = self.time_service.get_time()

        for event in self.event_list:
            self.process_events_due_now(time, event)

    def process_events_due_now(self, time, event):
        if event.is_in_use() and self.is_event_due_now(time, event):
            self.operate_light(event)
            event.reset_randomize()

    def is_event_due_now(self, time, event):
        todays_minute = event.minute_of_day + event.random_minutes
        day = event.day

        return time.matches_minute_of_day(todays_minute) and time.matches_day_of_week(day)

