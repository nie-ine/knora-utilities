#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.classes.Resource import Resource
from ...event.classes.Action import Action
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class human:Floruit

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class Floruit(Resource, Action):
    """
    Period during which a person or an Organisation was most active or
    flourishing.

    Labels: Floruit einer Person (de) / person's floruit (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Floruit"
