# --------------------------------------------------------------------------------------------------
# --------------------- Element | Components | The Classlist Descriptor Class ----------------------
# --------------------------------------------------------------------------------------------------
"""This module contains the Classlist class, a specialized subclass of Attribute and component of
the Element class.

"""

from typing import TYPE_CHECKING
from typing import Type

from types import FunctionType

if TYPE_CHECKING:
    from positron.Element.Bases.Element import Element as Element

from positron.Element.Components.Attribute import Attribute

class Classlist(Attribute):

    def __init__(self, decoratee: FunctionType):
        super().__init__(decoratee)

        self.attribute = 'classlist'
        self.markup    = 'className'

    def __get__(self, instance: 'Element' = None, prototype: Type['Element'] = None):

        if instance:
            return instance.attributes.get('classnames')

        return self

    def __set__(self, instance : 'Element', value: list[str]):
        instance.attributes.set('classnames', value)

    def __delete__(self, instance : 'Element'):
        instance.attributes.set('classnames', [])

    def format(self, instance: 'Element'):

        if classnames := instance.attributes.get('classnames'):

            representation : list[str] = []

            representation.append('class')
            representation.append('=')
            representation.append('"')
            representation.append(' '.join(classnames))
            representation.append('"')

            return ''.join(representation)

        return ''