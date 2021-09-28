# --------------------------------------------------------------------------------------------------
# --------------------- Element | Components | The Classname Descriptor Class ----------------------
# --------------------------------------------------------------------------------------------------
"""This module contains the Style class, a namespace class, populated with Attribute objects of its
own, and a component of the Element class.

"""

from typing import TYPE_CHECKING
from positron.Typing import Primitive

if TYPE_CHECKING:
    from positron.Element.Bases.Element import Element

from positron.Element.Components.Attributes import Attributes
from positron.Element.Components.Attribute import Attribute

import inspect
import contextlib_ext
import stringcase
import operator

attribute = Attribute

class Style(object):

    def __init__(self, element: 'Element'):

        self.element    = element
        self.attributes = Attributes(self)

    def format(self):

        representation : list[str] = []

        isAttribute = lambda member    : type(member) is Attribute
        valueOnly   = lambda member    : member[1]
        isNotNull   = lambda value     : value
        isNotEmpty  = lambda string    : string

        attributeDescriptors = inspect.getmembers(type(self), isAttribute)
        attributeDescriptors = map(valueOnly, attributeDescriptors)
        attributeDescriptors = filter(isNotNull, attributeDescriptors)

        formatter = lambda descriptor : descriptor.format(self)

        formatted = map(formatter, attributeDescriptors)
        formatted = filter(isNotEmpty, formatted)


        if formatted := ' '.join(list(formatted)):

            representation.append('style')
            representation.append('=')
            representation.append('"')
            representation.append(formatted)
            representation.append("")

            return ''.join(representation)

        return ''

    @attribute
    def display(self):
        ...

    @attribute
    def position(self):
        ...