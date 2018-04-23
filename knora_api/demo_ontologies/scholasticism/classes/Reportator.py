#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Role import Role
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class scholasticism:Reportator

created at: 2018-04-19 14:07:12
created from: scholasticism-ontology-knora.ttl
"""


class Reportator(Role):
    """
    Role of a scholastic student registering the content of a lesson.

    Labels: Reportator (de) / reportator (en) / reportator (la)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Reportator"
