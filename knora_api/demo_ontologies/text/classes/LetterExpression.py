#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Expression import Expression
from ...information_carrier.properties.isInLetter import IsInLetter
from ...text_structure.properties.hasStructure import HasStructure
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text:LetterExpression

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class LetterExpression(Expression):
    """
    Text expression with a letter structure.

    Labels: Brief-Expression (de) / letter expression (en)
    """
    def __init__(self, isInLetter=None, hasStructure=None, **kwargs):
        """

        :param isInLetter:
        :param hasStructure:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "LetterExpression"

        self.isInLetter = IsInLetter(isInLetter)
        self.hasStructure = HasStructure(hasStructure)
