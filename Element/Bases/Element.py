# --------------------------------------------------------------------------------------------------
# ---------------------------- Element | Bases | The Base Element Class ----------------------------
# --------------------------------------------------------------------------------------------------
"""This module contains the abstract base Element class, the base class from with all UI objects in
Positron's API inherit.

"""

from typing import TYPE_CHECKING
from typing import Union

if TYPE_CHECKING:
    from positron.Controllers.Document.Document import Document
    from positron.Controllers.Template.Template import Template

from positron.Element.Bases.Node import Node
from positron.Element.Bases.Target import Target
from positron.Element.Bases.Tag import Tag

from positron.Element.Components.Attribute import Attribute
from positron.Element.Components.Attributes import Attributes
from positron.Element.Components.Classlist import Classlist
from positron.Element.Components.Classname import Classname
from positron.Element.Components.Dataset import Dataset
from positron.Element.Components.Style import Style

attribute = Attribute
classlist = Classlist
classname = Classname

class Element(Tag, Target, Node):

    def __init__(self,
            document: Union['Document', 'Template'],
            tagname : str = 'element',
            xmlns   : str = 'www.positron.org/xmlns/element',
        ):

        super().__init__(document=document, tagname=tagname, xmlns=xmlns)

        self.attributes = Attributes(self)
        self.dataset    = Dataset(self)
        self.style      = Style(self)

        classnames : list[str] = []

        self.attributes.set('id', '')
        self.attributes.set('classnames', classnames)

    @attribute
    def id(self):
        ...

    @classlist
    def classlist(self):
        ...

    @classname
    def classname(self):
        ...

    @attribute
    def accesskey(self):
        ...

    @attribute
    def dir(self):
        ...

    @attribute
    def draggable(self, *, boolean : bool = True):
        ...

    @attribute
    def hidden(self, *, boolean : bool = True):
        ...

    @attribute
    def lang(self):
        ...

    @attribute
    def spellcheck(self, *, boolean : bool = True):
        ...

    @attribute
    def tabindex(self):
        ...

    @attribute
    def title(self):
        ...

    @attribute
    def translate(self):
        ...
