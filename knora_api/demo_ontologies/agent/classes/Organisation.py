#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Group import Group
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class agent:Organisation

created at: 2018-04-19 14:07:12
created from: agent-ontology-knora.ttl
"""


class Organisation(Group):
    """
    Organized group of agents.

    Label: organisation (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Organisation"
