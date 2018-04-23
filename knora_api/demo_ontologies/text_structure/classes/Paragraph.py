#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .CompositionalStructure import CompositionalStructure
from ..properties.isParagraphOf import IsParagraphOf
from ..properties.structureHasUnit import StructureHasUnit
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text-structure:Paragraph

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class Paragraph(CompositionalStructure):
    """
    Group of text lines.

    Labels: Paragraf (de) / paragraph (en)
    """
    def __init__(self, isParagraphOf=None, structureHasUnit=None, **kwargs):
        """

        :param isParagraphOf:
        :param structureHasUnit:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Paragraph"

        self.isParagraphOf = IsParagraphOf(isParagraphOf)
        self.structureHasUnit = StructureHasUnit(structureHasUnit)
