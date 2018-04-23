#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Agent import Agent
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class agent:Group

created at: 2018-04-19 14:07:12
created from: agent-ontology-knora.ttl
"""


class Group(Agent):
    """
    Group of agents.

    Label: group of agents (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Group"
