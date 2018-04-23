#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...event.classes.State import State
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class publishing:PublishingState

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class PublishingState(State):
    """
    State of an expression having been published or not.

    Labels: Publikationszustand (de) / publishing state (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PublishingState"
