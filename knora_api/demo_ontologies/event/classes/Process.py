#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Event import Event
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class event:Process

created at: 2018-04-19 14:07:12
created from: event-ontology-knora.ttl
"""


class Process(Event):
    """
    Event implying change, with an input and an output, in one or more steps.

    Labels: Verfahren (de) / process (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Process"
