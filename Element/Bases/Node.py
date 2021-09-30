from typing import TYPE_CHECKING
from typing import Optional
from typing import Union

if TYPE_CHECKING:
    from positron.Element.Bases.Element import Element

class Node(object):

    def __init__(self: 'Element'):

        self.parent   : Optional['Element'] = None
        self.children : list['Element']     = []

    def removeChild(self: 'Element', target: 'Element'):
        self.children.remove(target)

    def removeChildren(self: 'Element', *targets: 'Element'):
        tuple(map(self.children.remove, targets))

    def prependChild(self: 'Element', target: 'Element'):
        self.children[:0] = [target]

    def prependChildren(self: 'Element', *targets: 'Element'):
        self.children[:0] = targets

    def insertChildBefore(self: 'Element', reference: 'Element', target: 'Element'):
        self.children[(index := self.children.index(reference)): index] = [target]

    def insertChildrenBefore(self: 'Element', reference: 'Element', *targets: 'Element'):
        self.children[(index := self.children.index(reference)): index] = targets

    def insertChildAt(self: 'Element', index: int, target: 'Element'):
        self.children[index: index] = [target]

    def insertChildrenAt(self: 'Element', index: int, *targets: 'Element'):
        self.children[index: index] = targets

    def insertChildAfter(self: 'Element', reference: 'Element', target: 'Element'):
        self.children[(index := self.children.index(reference) + 1): index] = [target]

    def insertChildrenAfter(self: 'Element', reference: 'Element', *targets: 'Element'):
        self.children[(index := self.children.index(reference) + 1): index] = targets

    def appendChild(self: 'Element', target: 'Element'):
        self.children[len(self.children):] = [target]

    def appendChildren(self: 'Element', *targets: 'Element'):
        self.children[len(self.children):] = targets

    def cloneNode(self: 'Element') -> 'Element':

        clone = self.document.createElement(self.tagname)

        for name, attribute in self.attributes.items():
            setattr(clone, name, attribute)

        return clone

    def isAncestorOf(self: 'Element', target: 'Element') -> bool:

        while target is not None and target is not self:
            target = target.parent

        return target is self

    def isParentOf(self: 'Element', target: 'Element') -> bool:
        return target in self.children

    def isChildOf(self: 'Element', target: 'Element') -> bool:
        return self in target.children

    def isDescendantOf(self: 'Element', target: 'Element') -> bool:
        return target.isAncestorOf(self)

    @property
    def root(self: 'Element'):
        return self.document.root

    @property
    def isConnected(self: 'Element') -> bool:
        """Return a boolean indicating if this element is connected to it's document"""
        return self.isDescendantOf(self.root)

    @property
    def siblingIndex(self: 'Element') -> Optional[int]:

        return self.parent.children.index(self) if self.parent else None

    @property
    def firstSibling(self: 'Element') -> Optional['Element']:

        if not self.parent or (sibling := self.parent.firstChild) is self:
            return None

        return sibling

    @property
    def previousSibling(self: 'Element') -> Optional['Element']:

        if not self.parent or self.parent.firstChild is self:
            return None

        return self.parent.children[self.siblingIndex - 1]

    @property
    def nextSibling(self: 'Element') -> Optional['Element']:

        if not self.parent or self.parent.lastChild is self:
            return None

        return self.parent.children[self.siblingIndex + 1]

    @property
    def lastSibling(self: 'Element') -> Optional['Element']:

        if not self.parent or (sibling := self.parent.lastChild) is self:
            return None

        return sibling

    @property
    def firstChild(self: 'Element') -> Optional['Element']:
        return self.children[0] if self.children else None

    @property
    def lastChild(self: 'Element') -> Optional['Element']:
        return self.children[-1] if self.children else None
