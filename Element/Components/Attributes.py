# --------------------------------------------------------------------------------------------------
# --------------------- Element | Components | The Attributes Dictionary Class ---------------------
# --------------------------------------------------------------------------------------------------
"""This module contains the Attributes class, a dictionary-like component of the Element class.

"""

from typing import TYPE_CHECKING
from typing import Union

from positron.Typing import Primitive

if TYPE_CHECKING:
    from positron.Element.Bases.Element import Element
    from positron.Element.Components.Style import Style

from positron.Element.Components.Attribute import Attribute

import operator
import contextlib_ext
import inspect

class Attributes(object):

    def __init__(self, instance: Union['Element', 'Style']):

        self.instance = instance
        self.values   : dict[str, Primitive] = {}

    @contextlib_ext.suppress(KeyError)
    def get(self, attribute: str):
        return operator.getitem(self.values, attribute)

    @contextlib_ext.suppress(KeyError)
    def set(self, attribute: str, value: Primitive):
        operator.setitem(self.values, attribute, value)

    @contextlib_ext.suppress(KeyError)
    def delete(self, attribute: str):
        operator.delitem(self.values, attribute)

    def format(self, boolean: bool = False):

        representation : list[str] = []

        isAttribute = lambda member     : type(member) is Attribute
        valueOnly   = lambda member     : member[1]
        isTargeted  = lambda attribute  : attribute.boolean is boolean
        isNotNull   = lambda attribute  : self.get(attribute.markup)
        isNotId     = lambda attribute  : attribute.markup != 'id'
        isNotEmpty  = lambda string     : string

        attributeDescriptors = inspect.getmembers(type(self.instance), isAttribute)
        attributeDescriptors = map(valueOnly, attributeDescriptors)
        attributeDescriptors = filter(isTargeted, attributeDescriptors)
        attributeDescriptors = filter(isNotNull, attributeDescriptors)
        attributeDescriptors = filter(isNotId, attributeDescriptors)

        formatter = lambda descriptor : descriptor.format(self.instance)

        formatted = map(formatter, attributeDescriptors)
        formatted = filter(isNotEmpty, formatted)

        return ' '.join(formatted)