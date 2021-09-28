# --------------------------------------------------------------------------------------------------
# --------------------- Element | Components | The Classname Descriptor Class ----------------------
# --------------------------------------------------------------------------------------------------
"""This module contains the Dataset class, a dictionary-like component of the Element class.

"""

from typing import TYPE_CHECKING
from positron.Typing import Primitive

if TYPE_CHECKING:
    from positron.Element.Bases.Element import Element

class Dataset(object):

    def __init__(self, instance: 'Element'):

        self.instance = instance
        self.values   : dict[str, Primitive] = {}

    def format(self):
        return ''