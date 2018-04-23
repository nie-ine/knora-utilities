#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...literature.classes.Poem import Poem as lit_Poem
from .Text import Text
from ..properties.hasStrophe import HasStrophe
from ...text.properties.hasSpecialDescription import HasSpecialDescription
from ...human.properties.hasCreationDate import HasCreationDate
from ...text.properties.hasDetailDescription import HasDetailDescription
from ..properties.hasReferenceTitle import HasReferenceTitle
from ..properties.hasReferencePoem import HasReferencePoem
from ..properties.hasSameEditionAsIn import HasSameEditionAsIn
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:Poem

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class Poem(lit_Poem, Text):
    """
    Gedicht von Kuno Raeber.

    Labels: Gedicht (de) / poem (en)
    """
    def __init__(self, hasStrophe=None, hasSpecialDescription=None, hasCreationDate=None, hasDetailDescription=None, hasReferenceTitle=None, hasReferencePoem=None, hasSameEditionAsIn=None, **kwargs):
        """

        :param hasStrophe:
        :param hasSpecialDescription:
        :param hasCreationDate:
        :param hasDetailDescription:
        :param hasReferenceTitle:
        :param hasReferencePoem:
        :param hasSameEditionAsIn:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Poem"

        self.hasStrophe = HasStrophe(hasStrophe)
        self.hasSpecialDescription = HasSpecialDescription(hasSpecialDescription)
        self.hasCreationDate = HasCreationDate(hasCreationDate)
        self.hasDetailDescription = HasDetailDescription(hasDetailDescription)
        self.hasReferenceTitle = HasReferenceTitle(hasReferenceTitle)
        self.hasReferencePoem = HasReferencePoem(hasReferencePoem)
        self.hasSameEditionAsIn = HasSameEditionAsIn(hasSameEditionAsIn)
