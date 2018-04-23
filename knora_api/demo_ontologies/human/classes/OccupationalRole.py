#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Role import Role
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class human:OccupationalRole

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class OccupationalRole(Role):
    """
    Role of a person in an occupation.

    Labels: Tätigkeitsrolle (de) / occupational role (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "OccupationalRole"
