from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Callable
from typing import DefaultDict

if TYPE_CHECKING:
    from positron.Element.Bases.Element import Element

from positron.Element.Auxiliary.Event import Event

import collections
import operator

class Target(object):

    def __init__(self: 'Element'):
        super().__init__()

        eventListeners = collections.defaultdict(dict)
        self.eventListeners : DefaultDict[str, dict[Callable, Callable]] = eventListeners

    def addEventListener(self: 'Element', eventType: str, callback: Callable):
        operator.setitem(self.eventListeners.get(eventType), callback, callback)

    def removeEventListener(self: 'Element', eventType: str, callback: Callable):
        self.eventListeners.get(eventType).pop(callback)

    def removeEventListeners(self: 'Element', eventType: str):
        self.eventListeners.get(eventType).clear()

    def clearAllEventListeners(self: 'Element'):
        self.eventListeners = collections.defaultdict(dict)

    def dispatchEvent(self: 'Element', event: Event):

        callbacks = self.eventListeners.get(event.eventType).keys()
        [callback(self, event) for callback in callbacks]