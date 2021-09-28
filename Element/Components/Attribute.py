# --------------------------------------------------------------------------------------------------
# ------------------- Element | Components | The DOM Attribute Descriptor Class --------------------
# --------------------------------------------------------------------------------------------------
"""This module contains the Attribute class, a property-like descriptor and component of the Element
class.

"""

from typing import TYPE_CHECKING
from typing import Type
from typing import Union

from types import FunctionType
from positron.Typing import Primitive

if TYPE_CHECKING:
    from positron.Element.Bases.Element import Element as Element
    from positron.Element.Components.Style import Style

from positron.Element.Bases.Node import Node

import inspect
import stringcase

class Attribute(object):

    def __init__(self, decoratee: FunctionType):

        flags = inspect.getfullargspec(decoratee).kwonlydefaults or {}

        self.attribute = flags.get('attribute', decoratee.__name__)
        self.markup    = flags.get('markup',    stringcase.spinalcase(self.attribute))
        self.boolean   = flags.get('boolean',   False)

        self.decoratee = decoratee

    def __get__(self,
            instance    : Union['Element', 'Style'] = None,
            prototype   : Union[Type['Element'], Type['Style']] = None,
        ):

        if instance:
            return instance.attributes.get(self.markup)

        return self

    def __set__(self, instance : Union['Element', 'Style'], value: Primitive):
        instance.attributes.set(self.markup, value)

    def __delete__(self, instance : Union['Element', 'Style']):
        instance.attributes.set(self.markup)

    def format(self, instance: Union['Element', 'Style']):

        value = instance.attributes.get(self.markup)

        if value and not self.boolean:

            representation : list[str] = []

            representation.append(self.markup)
            representation.append('=')
            representation.append('"')
            representation.append(value)
            representation.append('"')

            return ''.join(representation)

        elif value:
            return self.markup

        return ''