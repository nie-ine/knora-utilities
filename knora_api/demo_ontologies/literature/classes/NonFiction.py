#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...concept.classes.NonFiction import NonFiction as con_NonFiction
from .Literature import Literature
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class literature:NonFiction

created at: 2018-04-19 14:07:12
created from: literature-ontology-knora.ttl
"""


class NonFiction(con_NonFiction, Literature):
    """
    Literature having content based on fact.

    Labels: sachliche Literatur (de) / literary non-fiction (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "NonFiction"
