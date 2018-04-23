#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Process import Process
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class event:Action

created at: 2018-04-19 14:07:12
created from: event-ontology-knora.ttl
"""


class Action(Process):
    """
    Process involving one or more agents causing change.

    Labels: Aktion (de) / action (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Action"
