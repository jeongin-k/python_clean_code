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

    def notify_unregistration(self, old_observer):
        pass

class EventDispatcher:
    def __init__(self):
        self.observer_list = []

    def register_observer(self, event_type, observer):
        for existing_observer in self.observer_list:
            print(existing_observer)
            existing_observer[1].notify_registration(observer)

        self.observer_list.append((event_type, observer))

    def unregister_observer(self, event_type, observer):
        target = None

        for entry in self.observer_list:
            current_type, current_observer = entry

            if current_observer != observer:
                current_observer.notify_unregistration(observer)
            elif event_type == current_type:
                target = entry

        if target:
            self.observer_list.remove(target)

    def dispatch_event(self, event, timeout_seconds):
        for event_type, observer in self.observer_list:
            if event_type == event.type:
                observer.notify(event, timeout_seconds)

