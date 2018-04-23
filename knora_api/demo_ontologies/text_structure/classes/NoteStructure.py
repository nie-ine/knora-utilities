#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Structure import Structure
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text-structure:NoteStructure

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class NoteStructure(Structure):
    """
    Text with note structure, not having a unit such as a sentence.

    Labels: Notiz-Struktur (de) / note structure (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "NoteStructure"
