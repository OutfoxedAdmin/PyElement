from __future__ import annotations

from typing import TYPE_CHECKING
from positron.Typing import Primitive

if TYPE_CHECKING:
    from positron.Element.Bases.Element import Element as Element

from positron.Element.Components.Attribute import Attribute

import operator
import inspect

class Dataset(object):

    def __init__(self, instance: 'Element'):

        self.instance = instance
        self.values   : dict[str, Primitive] = {}

    def get(self, attribute: str):
        return operator.getitem(self.values, attribute)

    def __getitem__(self, attribute: str):
        return operator.getitem(self.values, attribute)

    def set(self, attribute: str, value: Primitive):
        return operator.setitem(self.values, attribute, value)

    def __setitem__(self, attribute: str, value: Primitive):
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

    def format(self):

        representation : list[str] = []

        for attribute, value in self.items():
            representation.append(f'{attribute}="{value}"')

        return ' '.join(representation)