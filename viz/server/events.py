import json
import queue
import threading


class EventBroker:
    def __init__(self):
        self._subscribers = set()
        self._lock = threading.Lock()

    def subscribe(self):
        subscriber = queue.Queue()
        with self._lock:
            self._subscribers.add(subscriber)
        return subscriber

    def unsubscribe(self, subscriber):
        with self._lock:
            self._subscribers.discard(subscriber)

    def publish(self, event, payload):
        message = (event, json.dumps(payload, ensure_ascii=False))
        with self._lock:
            subscribers = tuple(self._subscribers)
        for subscriber in subscribers:
            subscriber.put(message)
