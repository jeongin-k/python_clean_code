from eventdispatcher import Event
from eventdispatcher import EventType
from eventdispatcher import EventDispatcher
from eventdispatcher import EventObserver
import unittest
from unittest import mock
from unittest.mock import Mock

class ObserverMock(EventObserver):
    def __init__(self):
        self.mock = Mock()

    def notify(self, event, time_out_in_seconds):
        self.mock.notify(event, time_out_in_seconds)

    def notify_registration(self, new_observer):
        self.mock.notify_registration(new_observer)

class TestEventDispatcher(unittest.TestCase):
    def setUp(self):
        self.event = Event(EventType.IMPORTANT_EVENT)
        self.dispatcher = EventDispatcher()
        self.observer = ObserverMock()
        self.observer2 = ObserverMock()

    def tearDown(self):
        pass

    def test_event_without_registrations_results_into_no_calls(self):
        self.dispatcher.dispatch_event(self.event, 10)

    def test_event_with_registration_for_event_results_into_callback(self):
        with mock.patch.object(self.observer.mock, 'notify') as mock_notify:
            self.event.type = EventType.IMPORTANT_EVENT

            self.dispatcher.register_observer(EventType.IMPORTANT_EVENT, self.observer)
            self.dispatcher.dispatch_event(self.event, 10)

            mock_notify.assert_called_once_with(self.event, 10)

    def test_different_event_with_registration_does_not_result_into_callback(self):
        self.event.type = EventType.LESS_IMPORTANT_EVENT
        self.dispatcher.register_observer(EventType.IMPORTANT_EVENT, self.observer)
        self.dispatcher.dispatch_event(self.event, 10)

    def test_register_two_observers_results_into_two_calls_and_registration_notification(self):
        with mock.patch.object(self.observer.mock, 'notify') as mock_notify, \
             mock.patch.object(self.observer2.mock, 'notify') as mock_notify2, \
             mock.patch.object(self.observer.mock, 'notify_registration') as mock_registration:

            self.event.type = EventType.IMPORTANT_EVENT
            self.dispatcher.register_observer(EventType.IMPORTANT_EVENT, self.observer)
            self.dispatcher.register_observer(EventType.IMPORTANT_EVENT, self.observer2)
            self.dispatcher.dispatch_event(self.event, 10)

            mock_notify.assert_called_once_with(self.event, 10)
            mock_notify2.assert_called_once_with(self.event, 10)
            mock_registration.assert_called_once_with(self.observer2)

if __name__ == '__main__':
    unittest.main()
