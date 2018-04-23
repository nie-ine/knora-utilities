#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...agent.classes.Agent import Agent
from ..properties.hasBiologicalSex import HasBiologicalSex
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class human:Human

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class Human(Agent):
    """
    Member of the subspecies Homo sapiens sapiens.

    Labels: Mensch (de) / human (en) / homme (fr) / huomo (it)
    """
    def __init__(self, hasBiologicalSex=None, **kwargs):
        """

        :param hasBiologicalSex:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Human"

        self.hasBiologicalSex = HasBiologicalSex(hasBiologicalSex)
