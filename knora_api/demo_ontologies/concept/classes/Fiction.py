#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Concept import Concept
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class concept:Fiction

created at: 2018-04-19 14:07:12
created from: concept-ontology-knora.ttl
"""


class Fiction(Concept):
    """
    Concept derived from imagination.

    Labels: Fiktion (de) / fiction (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Fiction"
