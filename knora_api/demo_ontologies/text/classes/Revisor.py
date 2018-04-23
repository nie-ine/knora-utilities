#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.Role import Role
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text:Revisor

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class Revisor(Role):
    """
    Role of a person checking on certain aspects of a text.

    Labels: Revisor (de) / revisor (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Revisor"
