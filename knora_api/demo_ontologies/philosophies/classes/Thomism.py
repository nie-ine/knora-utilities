#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...philosophy.classes.Philosophy import Philosophy
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class philosophies:Thomism

created at: 2018-04-19 14:07:12
created from: philosophies-ontology-knora.ttl
"""


class Thomism(Philosophy):
    """
    .

    Label: Thomism (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Thomism"
