from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from positron.Element.Bases.Element import Element

from positron.Element.Bases.Node import Node
from positron.Element.Bases.Target import Target

class Tag(Target, Node):

    def __str__(self: 'Element'):
        ...






