#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.classes.Expression import Expression
from ..properties.isFinalVersion import IsFinalVersion
from ...knora_base.properties.seqnum import Seqnum
from ..properties.isPartOfCycle import IsPartOfCycle
from ..properties.hasEdition import HasEdition
from ..properties.isInSwissGerman import IsInSwissGerman
from ...text.properties.hasAuthor import HasAuthor
from ...text.properties.hasAlias import HasAlias
from ...text.properties.hasTitle import HasTitle
from ...human.properties.hasModificationDate import HasModificationDate
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:Text

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class Text(Expression):
    """
    Text authored by Kuno Raeber.

    Labels: Text-Expression (de) / text expression (en)
    """
    def __init__(self, isFinalVersion=None, seqnum=None, isPartOfCycle=None, hasEdition=None, isInSwissGerman=None, hasAuthor=None, hasAlias=None, hasTitle=None, hasModificationDate=None, **kwargs):
        """

        :param isFinalVersion:
        :param seqnum:
        :param isPartOfCycle:
        :param hasEdition:
        :param isInSwissGerman:
        :param hasAuthor:
        :param hasAlias:
        :param hasTitle:
        :param hasModificationDate:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Text"

        self.isFinalVersion = IsFinalVersion(isFinalVersion)
        self.seqnum = Seqnum(seqnum)
        self.isPartOfCycle = IsPartOfCycle(isPartOfCycle)
        self.hasEdition = HasEdition(hasEdition)
        self.isInSwissGerman = IsInSwissGerman(isInSwissGerman)
        self.hasAuthor = HasAuthor(hasAuthor)
        self.hasAlias = HasAlias(hasAlias)
        self.hasTitle = HasTitle(hasTitle)
        self.hasModificationDate = HasModificationDate(hasModificationDate)
