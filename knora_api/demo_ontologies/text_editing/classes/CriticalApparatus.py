#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.classes.Expression import Expression
from ..properties.isApparatusOf import IsApparatusOf
from ...text_structure.properties.hasStructure import HasStructure
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text-editing:CriticalApparatus

created at: 2018-04-19 14:07:12
created from: text-editing-ontology-knora.ttl
"""


class CriticalApparatus(Expression):
    """
    Note to a critical text edition providing information of a textual version.

    Labels: kritischer Apparat (de) / critical apparatus (en) / apparatus criticus (la)
    """
    def __init__(self, isApparatusOf=None, hasStructure=None, **kwargs):
        """

        :param isApparatusOf:
        :param hasStructure:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "CriticalApparatus"

        self.isApparatusOf = IsApparatusOf(isApparatusOf)
        self.hasStructure = HasStructure(hasStructure)
