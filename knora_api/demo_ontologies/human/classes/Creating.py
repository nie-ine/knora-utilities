#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...event.classes.Creating import Creating as eve_Creating
from .Action import Action
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class human:Creating

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class Creating(eve_Creating, Action):
    """
    Action by a person bringing something into existence.

    Labels: Kreierung einer Person (de) / person's creating (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Creating"
