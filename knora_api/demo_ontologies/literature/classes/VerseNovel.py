#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Epic import Epic
from ...text.classes.Expression import Expression
from .Fiction import Fiction
from ...text_structure.properties.hasStructure import HasStructure
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class literature:VerseNovel

created at: 2018-04-19 14:07:12
created from: literature-ontology-knora.ttl
"""


class VerseNovel(Epic, Expression, Fiction):
    """
    Epic fiction expression in verse and with novel-length.

    Labels: Versroman (de) / verse novel (en)
    """
    def __init__(self, hasStructure=None, **kwargs):
        """

        :param hasStructure:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "VerseNovel"

        self.hasStructure = HasStructure(hasStructure)
