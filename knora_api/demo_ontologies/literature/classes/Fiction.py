#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...concept.classes.Fiction import Fiction as con_Fiction
from .Literature import Literature
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class literature:Fiction

created at: 2018-04-19 14:07:12
created from: literature-ontology-knora.ttl
"""


class Fiction(con_Fiction, Literature):
    """
    Literature having content derived from imagination.

    Labels: literarische Fiktion (de) / literary fiction (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Fiction"
