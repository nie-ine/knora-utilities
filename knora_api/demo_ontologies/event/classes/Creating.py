#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Action import Action
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class event:Creating

created at: 2018-04-19 14:07:12
created from: event-ontology-knora.ttl
"""


class Creating(Action):
    """
    Bringing into existence.

    Labels: Kreierung (de) / creating (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Creating"
