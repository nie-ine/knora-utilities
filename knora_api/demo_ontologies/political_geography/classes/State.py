#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...organisation.classes.PoliticalOrganization import PoliticalOrganization
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class political-geography:State

created at: 2018-04-19 14:07:12
created from: political-geography-ontology-knora.ttl
"""


class State(PoliticalOrganization):
    """
    Political organization of a nation with an own government.

    Labels: Staat (de) / state (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "State"
