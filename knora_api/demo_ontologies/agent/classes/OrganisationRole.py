#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .GroupRole import GroupRole
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class agent:OrganisationRole

created at: 2018-04-19 14:07:12
created from: agent-ontology-knora.ttl
"""


class OrganisationRole(GroupRole):
    """
    Role of an Organisation.

    Label: organisation role (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "OrganisationRole"
