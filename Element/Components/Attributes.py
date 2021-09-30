from __future__ import annotations

import inspect
from typing import TYPE_CHECKING
from positron.Typing import Primitive

if TYPE_CHECKING:
    from positron.Element.Bases.Element import Element as Element
    from positron.Element.Components.Classnames import Classnames
    from positron.Element.Components.Style import Style

from positron.Element.Components.Attribute import Attribute

import operator

class Attributes(object):

    def __init__(self, instance: 'Element | Style'):

        self.instance = instance
        self.values   : dict[str, 'Primitive | Classnames'] = {}

    def get(self, attribute: str):
        return operator.getitem(self.values, attribute)

    def __getitem__(self, attribute: str):
        return operator.getitem(self.values, attribute)

    def set(self, attribute: str, value: 'Primitive | Classnames'):
        return operator.setitem(self.values, attribute, value)

    def __setitem__(self, attribute: str, value: 'Primitive | Classnames'):
        return operator.setitem(self.values, attribute, value)

    def delete(self, attribute: str):
        return operator.delitem(self.values, attribute)

    def __delitem__(self, attribute: str):
        return operator.delitem(self.values, attribute)

    def __contains__(self, attribute: str):
        return attribute in self.values

    def __iter__(self):
        return iter(self.values)

    def __bool__(self):
        return bool(self.values)

    def items(self):
        return self.values.items()

    def keys(self):
        return self.values.keys()

    def values(self):
        return self.values.values()

    def format(self, boolean: bool = False):

        representation : list[str] = []

        for member, descriptor in inspect.getmembers(type(self.instance)):

            if not isinstance(descriptor, Attribute):
                continue

            if not (value := self.get(descriptor.markupCase)):
                continue

            if descriptor.boolean is not boolean:
                continue

            if descriptor.omitted:
                continue

            representation.append(descriptor.format(value))

        return ' '.join(representation)