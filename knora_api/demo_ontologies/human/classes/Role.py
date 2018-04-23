#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...agent.classes.Role import Role as age_Role
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class human:Role

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class Role(age_Role):
    """
    A role a person has as a social entity.

    Labels: Rolle einer Person (de) / person role (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Role"
