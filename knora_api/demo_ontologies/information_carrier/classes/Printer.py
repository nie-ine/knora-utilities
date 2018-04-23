#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.Role import Role
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:Printer

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class Printer(Role):
    """
    Role of a person printing a text.

    Labels: Drucker (de) / printer (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Printer"
