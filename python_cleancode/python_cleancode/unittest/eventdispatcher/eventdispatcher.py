from enum import Enum

class EventType(Enum):
    IMPORTANT_EVENT = 1
    LESS_IMPORTANT_EVENT = 2

class Event:
    def __init__(self, event_type):
        self.type = event_type

class EventObserver:
    def __init__(self):
        pass

    def notify(self, event, timeout_seconds):
        pass

    def notify_registration(self, new_observer):
        pass

class EventDispatcher:
    def __init__(self):
        self.observer_list = []

    def register_observer(self, event_type, observer):
        for existing_observer in self.observer_list:
            print(existing_observer)
            existing_observer[1].notify_registration(observer)

        self.observer_list.append((event_type, observer))

    def dispatch_event(self, event, timeout_seconds):
        for event_type, observer in self.observer_list:
            if event_type == event.type:
                observer.notify(event, timeout_seconds)

