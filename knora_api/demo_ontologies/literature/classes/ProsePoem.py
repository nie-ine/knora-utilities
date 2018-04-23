#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Poem import Poem
from .Epic import Epic
from ...text_structure.properties.hasStructure import HasStructure
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class literature:ProsePoem

created at: 2018-04-19 14:07:12
created from: literature-ontology-knora.ttl
"""


class ProsePoem(Poem, Epic):
    """
    Gedicht in Prosa geschrieben.

    Labels: Prosagedicht (de) / prose poem (en)
    """
    def __init__(self, hasStructure=None, **kwargs):
        """

        :param hasStructure:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "ProsePoem"

        self.hasStructure = HasStructure(hasStructure)
