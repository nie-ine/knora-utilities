#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .SyntacticStructure import SyntacticStructure
from ..properties.structureHasUnit import StructureHasUnit
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text-structure:Prose

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class Prose(SyntacticStructure):
    """
    Syntactic structure with a sentence as unit, in a natural flow of speech.

    Labels: Prosa (de) / prose (en)
    """
    def __init__(self, structureHasUnit=None, **kwargs):
        """

        :param structureHasUnit:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Prose"

        self.structureHasUnit = StructureHasUnit(structureHasUnit)
