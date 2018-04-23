#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Structure import Structure
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text-structure:CompositionalStructure

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class CompositionalStructure(Structure):
    """
    Text structure depending on text composition in a two-dimensional plane,
    e.g. a header, line, paragraph, page, chapter.

    Labels: kompositionelle Textstruktur (de) / compositional text structure (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "CompositionalStructure"
