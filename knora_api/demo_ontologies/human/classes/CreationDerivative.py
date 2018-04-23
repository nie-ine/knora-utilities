#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Creation import Creation
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class human:CreationDerivative

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class CreationDerivative(Creation):
    """
    Derivative of a person's creation, e.g. a translation.

    Labels: Derivat einer Kreation (de) / creation derivative (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "CreationDerivative"
