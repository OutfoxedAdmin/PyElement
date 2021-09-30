from __future__ import annotations

from positron.Element.Components.Attribute import Attribute
from positron.Element.Components.Attributes import Attributes
from positron.Element.Components.Classnames import Classnames
from positron.Element.Components.Dataset import Dataset
from positron.Element.Components.Style import Style

from positron.Element.Bases.Node import Node
from positron.Element.Bases.Target import Target
from positron.Element.Bases.Tag import Tag

class Element(Tag, Target, Node):

    def __init__(self,
            document: 'Document | Template',
            xmlns   : str = 'www.positron.org/namespaces/xml',
            tagname : str = 'xml-element',
        ):

        super().__init__()  # continue the constructor chain

        self.attributes = Attributes(self)
        self.dataset    = Dataset(self)
        self.style      = Style(self)

        self.document   = document
        self.xmlns      = xmlns
        self.tagname    = tagname

        self.attributes.set('classname', Classnames(self))

    id        = Attribute('id', omitted=True)
    classlist = Classnames.Classlist()
    classname = Classnames.Classname()

    accesskey       = Attribute('accesskey')
    contenteditable = Attribute('contenteditable', boolean=True)
    dir             = Attribute('dir')
    draggable       = Attribute('draggable', boolean=True)
    hidden          = Attribute('hidden', boolean=True)
    lang            = Attribute('lang')
    spellcheck      = Attribute('spellcheck', boolean=True)
    tabindex        = Attribute('tabindex')
    title           = Attribute('title')
    translate       = Attribute('translate')