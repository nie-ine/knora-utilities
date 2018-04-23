#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Poem import Poem
from ...text_structure.properties.hasStructure import HasStructure
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class literature:VersePoem

created at: 2018-04-19 14:07:12
created from: literature-ontology-knora.ttl
"""


class VersePoem(Poem):
    """
    Gedicht ausgedruckt in Vers.

    Labels: Versgedicht (de) / verse poem (en)
    """
    def __init__(self, hasStructure=None, **kwargs):
        """

        :param hasStructure:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "VersePoem"

        self.hasStructure = HasStructure(hasStructure)
