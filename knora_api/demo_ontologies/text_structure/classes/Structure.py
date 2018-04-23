#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...language.classes.HumanNaturalLanguageExpression import HumanNaturalLanguageExpression
from ..properties.structureHasUnit import StructureHasUnit
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text-structure:Structure

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class Structure(HumanNaturalLanguageExpression):
    """
    Human natural language expression as structure, e.g. a word, sentence, text
    line, paragraph, verse, strophe.

    Labels: Textstruktur (de) / text structure (en)
    """
    def __init__(self, structureHasUnit=None, **kwargs):
        """

        :param structureHasUnit:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Structure"

        self.structureHasUnit = StructureHasUnit(structureHasUnit)
