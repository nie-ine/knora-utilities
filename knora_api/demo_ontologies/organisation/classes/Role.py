#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...agent.classes.Role import Role as age_Role
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class organisation:Role

created at: 2018-04-19 14:07:12
created from: organisation-ontology-knora.ttl
"""


class Role(age_Role):
    """
    Role of a person organisation.

    Label: organisation role (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Role"
