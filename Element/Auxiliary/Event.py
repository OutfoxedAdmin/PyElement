# --------------------------------------------------------------------------------------------------
# ----------------------- Element | Auxiliary | The Event Data Carrier Class -----------------------
# --------------------------------------------------------------------------------------------------
"""This module contains the Event class, a data-carrier class used in close conjunction with Element
objects, to signal and carry information about user interactions with sed elements.

"""

from positron.Typing import Primitive

class Event(object):

    def __init__(self, eventType: str, **eventData: Primitive):

        self.eventType  = eventType

        self.target         = eventData.get('target', None)
        self.originalTarget = eventData.get('originalTarget', None)