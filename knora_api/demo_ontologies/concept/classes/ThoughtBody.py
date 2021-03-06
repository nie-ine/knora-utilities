#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .PropositionalConcept import PropositionalConcept
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class concept:ThoughtBody

created at: 2018-04-19 14:07:12
created from: concept-ontology-knora.ttl
"""


class ThoughtBody(PropositionalConcept):
    """
    .

    Labels: Gedankengut (de) / body of thought (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "ThoughtBody"
