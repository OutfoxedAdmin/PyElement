from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Type

from positron.Typing import Primitive

if TYPE_CHECKING:
    from positron.Element.Bases.Element import Element as Element
    from positron.Element.Components.Style import Style

AttributedType  = Type['Element | Style']
Attributed      = 'Element | Style'

class Attribute(object):

    def __init__(self, markupCase: str, boolean: bool = False, omitted: bool = False):

        self.markupCase = markupCase
        self.camelCase  = ''

        self.boolean = boolean
        self.omitted = omitted

    def __set_name__(self, owner: AttributedType, camelCase: str):

        self.camelCase = camelCase

    def __get__(self, instance: Attributed = None, prototype: AttributedType = None):

        if instance:
            return instance.attributes.get(self.markupCase)

        return self

    def __set__(self, instance: Attributed, value: Primitive):
        instance.attributes.set(self.markupCase, value)

    def __delete__(self, instance: Attributed):
        instance.attributes.delete(self.markupCase)

    def format(self, value: Primitive):

        if self.boolean:
            return self.markupCase

        return f'{self.markupCase}="{value}"'