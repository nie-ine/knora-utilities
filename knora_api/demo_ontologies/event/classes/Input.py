#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.classes.Resource import Resource
from ..properties.event:isInputOf import Event:isInputOf
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class event:Input

created at: 2018-04-19 14:07:12
created from: event-ontology-knora.ttl
"""


class Input(Resource):
    """
    Precondition to a change in a process.

    Labels: Input (de) / input (en)
    """
    def __init__(self, event:isInputOf=None, **kwargs):
        """

        :param event:isInputOf:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Input"

        self.event:isInputOf = Event:isInputOf(event:isInputOf)
