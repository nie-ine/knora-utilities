#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Action import Action
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class event:Procedure

created at: 2018-04-19 14:07:12
created from: event-ontology-knora.ttl
"""


class Procedure(Action):
    """
    Action executed in one or more steps, in a certain manner obtaining a
    certain output under certain circumstances.

    Labels: Vorgehen (de) / procedure (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Procedure"
