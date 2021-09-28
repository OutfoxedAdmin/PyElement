# --------------------------------------------------------------------------------------------------
# ------------------------ Element | Bases | The Abstract Base Target Class ------------------------
# --------------------------------------------------------------------------------------------------
"""This module contains the abstract base Target class, a base of the Element class.

"""

from typing import TYPE_CHECKING
from typing import Callable
from typing import DefaultDict
from typing import Union

if TYPE_CHECKING:
    from positron.Controllers.Document.Document import Document
    from positron.Controllers.Template.Template import Template

from positron.Element.Bases.Node import Node
from positron.Element.Auxiliary.Event import Event

import collections
import operator

class Target(Node):

    def __init__(self,
            document: Union['Document', 'Template'],
            tagname: str = 'element',
            xmlns: str = 'www.positron.org/xmlns/element',
        ):

        super().__init__(document=document, tagname=tagname, xmlns=xmlns)

        eventListeners = collections.defaultdict(dict)
        self.eventListeners : DefaultDict[str, dict[Callable, Callable]] = eventListeners

    def addEventListener(self, eventType: str, callback: Callable):
        operator.setitem(self.eventListeners.get(eventType), callback, callback)

    def removeEventListener(self, eventType: str, callback: Callable):
        self.eventListeners.get(eventType).pop(callback)

    def removeEventListeners(self, eventType: str):
        self.eventListeners.get(eventType).clear()

    def clearAllEventListeners(self):
        self.eventListeners = collections.defaultdict(dict)

    def dispatchEvent(self, event: Event):

        callbacks = self.eventListeners.get(event.eventType).keys()
        [callback(self, event) for callback in callbacks]