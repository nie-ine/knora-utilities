#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.Creation import Creation
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class concept:Concept

created at: 2018-04-19 14:07:12
created from: concept-ontology-knora.ttl
"""


class Concept(Creation):
    """
    Abstract idea created by a person.

    Labels: Konzept (de) / concept (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Concept"
