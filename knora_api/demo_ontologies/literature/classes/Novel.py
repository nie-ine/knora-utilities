#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.classes.Expression import Expression
from .Epic import Epic
from .Fiction import Fiction
from ...text_structure.properties.hasStructure import HasStructure
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class literature:Novel

created at: 2018-04-19 14:07:12
created from: literature-ontology-knora.ttl
"""


class Novel(Expression, Epic, Fiction):
    """
    Epic fiction expression.

    Labels: Roman (de) / novel (en)
    """
    def __init__(self, hasStructure=None, **kwargs):
        """

        :param hasStructure:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Novel"

        self.hasStructure = HasStructure(hasStructure)
