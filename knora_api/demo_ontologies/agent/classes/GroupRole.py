#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Role import Role
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class agent:GroupRole

created at: 2018-04-19 14:07:12
created from: agent-ontology-knora.ttl
"""


class GroupRole(Role):
    """
    Role of a group.

    Label: group role (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "GroupRole"
