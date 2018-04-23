#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Concept import Concept
from ..properties.isPartOf import IsPartOf
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class concept:SymbolicConcept

created at: 2018-04-19 14:07:12
created from: concept-ontology-knora.ttl
"""


class SymbolicConcept(Concept):
    """
    Concept represented by one or more symbols.

    Labels: symbolisches Konzept (de) / symbolic concept (en)
    """
    def __init__(self, isPartOf=None, **kwargs):
        """

        :param isPartOf:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "SymbolicConcept"

        self.isPartOf = IsPartOf(isPartOf)
