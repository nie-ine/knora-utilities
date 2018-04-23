#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .CompositionalStructure import CompositionalStructure
from ..properties.isLineOf import IsLineOf
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text-structure:Line

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class Line(CompositionalStructure):
    """
    Text structure composed as a line.

    Labels: Textzeile (de) / text line (en)
    """
    def __init__(self, isLineOf=None, **kwargs):
        """

        :param isLineOf:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Line"

        self.isLineOf = IsLineOf(isLineOf)
