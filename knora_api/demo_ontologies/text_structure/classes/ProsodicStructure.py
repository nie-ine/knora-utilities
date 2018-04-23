#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Structure import Structure
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text-structure:ProsodicStructure

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class ProsodicStructure(Structure):
    """
    Text structure depending on prosody, i.e. metre as basic rhythmic
    structure, rhyme and syllable.

    Labels: prosodische Textstruktur (de) / prosodic text structure (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "ProsodicStructure"
