#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Role import Role
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class human:Creator

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class Creator(Role):
    """
    Role of a person creating something.

    Labels: Erschaffer (de) / creator (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Creator"
