#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .PropositionalConcept import PropositionalConcept
from ..properties.isExpressedIn import IsExpressedIn
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class concept:Work

created at: 2018-04-19 14:07:12
created from: concept-ontology-knora.ttl
"""


class Work(PropositionalConcept):
    """
    Intellectual product as concept.

    Labels: Werk (de) / work (en)
    """
    def __init__(self, isExpressedIn=None, **kwargs):
        """

        :param isExpressedIn:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Work"

        self.isExpressedIn = IsExpressedIn(isExpressedIn)
