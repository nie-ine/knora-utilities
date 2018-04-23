#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.classes.WrittenText import WrittenText
from .Text import Text
from ...text.classes.LetterExpression import LetterExpression as tex_LetterExpression
from ...text.properties.hasSpecialDescription import HasSpecialDescription
from ...publishing.properties.hasPublishingState import HasPublishingState
from ...human.properties.hasCreationDate import HasCreationDate
from ...text_structure.properties.hasStructure import HasStructure
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:LetterExpression

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class LetterExpression(WrittenText, Text, tex_LetterExpression):
    """
    Letter expression written by Kuno Raeber.

    Labels: Brief-Expression (de) / letter expression (en)
    """
    def __init__(self, hasSpecialDescription=None, hasPublishingState=None, hasCreationDate=None, hasStructure=None, **kwargs):
        """

        :param hasSpecialDescription:
        :param hasPublishingState:
        :param hasCreationDate:
        :param hasStructure:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "LetterExpression"

        self.hasSpecialDescription = HasSpecialDescription(hasSpecialDescription)
        self.hasPublishingState = HasPublishingState(hasPublishingState)
        self.hasCreationDate = HasCreationDate(hasCreationDate)
        self.hasStructure = HasStructure(hasStructure)
