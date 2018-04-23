#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...agent.classes.Role import Role
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class publishing:Publisher

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class Publisher(Role):
    """
    Role of an agent as publisher.

    Labels: Herausgeber (de) / publisher (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Publisher"
