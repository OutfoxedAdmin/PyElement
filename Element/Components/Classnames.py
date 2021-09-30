from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Type

if TYPE_CHECKING:
    from positron.Element.Bases.Element import Element

from positron.Element.Components.Attribute import Attribute

import operator

class Classnames(object):

    class Classname(Attribute):

        def __init__(self):
            super().__init__(attribute='classnames', omitted=True)

        def __get__(self, instance: 'Element' = None, prototype: Type['Element'] = None):

            if instance:
                return ' '.join(instance.attributes.get('classnames'))

            return self

        def __set__(self, instance: 'Element', classname: str):
            instance.attributes.get('classnames').set(classname.split())

        def __delete__(self, instance: 'Element'):
            instance.attributes.get('classnames').set([])

    class Classlist(Attribute):

        def __init__(self):
            super().__init__(attribute='classnames', omitted=True)

        def __get__(self, instance: 'Element' = None, prototype: Type['Element'] = None):

            if instance:
                return instance.attributes.get('classnames')

            return self

        def __set__(self, instance: 'Element', classnames: list[str]):
            instance.attributes.get('classnames').set(classnames)

        def __delete__(self, instance: 'Element'):
            instance.attributes.get('classnames').set([])

    def __init__(self, element: 'Element'):

        self.element    = element
        self.classnames : list[str] = []

    def get(self, index: int):
        return operator.getitem(self.classnames, index)

    def __getitem__(self, index: int):
        return operator.getitem(self.classnames, index)

    def set(self, index: int, classname: str):
        return operator.setitem(self.classnames, index, classname)

    def __setitem__(self, index: int, classname: str):
        return operator.setitem(self.classnames, index, classname)

    def delete(self, index: int):
        return operator.delitem(self.classnames, index)

    def __delitem__(self, index: int):
        return operator.delitem(self.classnames, index)

    def __contains__(self, classname: str):
        return classname in self.classnames

    def __iter__(self):
        return iter(self.classnames)

    def __bool__(self):
        return bool(self.classnames)
