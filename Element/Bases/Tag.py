# --------------------------------------------------------------------------------------------------
# ------------------------- Element | Bases | The Abstract Base Tag Class --------------------------
# --------------------------------------------------------------------------------------------------
"""This module contains the abstract base Tag class, a base of the Element class.

"""

from typing import TYPE_CHECKING
from typing import Union

if TYPE_CHECKING:
    from positron.Controllers.Document.Document import Document
    from positron.Controllers.Template.Template import Template
    from positron.Element.Bases.Element import Element

from positron.Element.Bases.Node import Node
from positron.Element.Bases.Target import Target

class Tag(Target, Node):

    def __init__(self,
            document: Union['Document', 'Template'],
            tagname : str = 'element',
            xmlns   : str = 'www.positron.org/xmlns/element',
        ):

        super().__init__(document=document, tagname=tagname, xmlns=xmlns)

    def __str__(self: 'Element'):

        representation : list[str] = []

        representation.append(self.tagname)
        representation.append(type(self).id.format(self))
        representation.append(type(self).classname.format(self))
        representation.append(self.style.format())
        representation.append(self.attributes.format(boolean=False))
        representation.append(self.dataset.format())
        representation.append(self.attributes.format(boolean=True))

        representation = filter(lambda string : string, representation)

        return ''.join(('<', ' '.join(representation), '>'))

    def __repr__(self):
        return str(self)