#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...event.classes.Action import Action as eve_Action
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class human:Action

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class Action(eve_Action):
    """
    Action with a human agent.

    Labels: menschliche Aktion (de) / human action (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Action"
