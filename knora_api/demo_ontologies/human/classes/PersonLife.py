#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...event.classes.Existence import Existence
from ...event.classes.Action import Action
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class human:PersonLife

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class PersonLife(Existence, Action):
    """
    Life of a human from birth until death.

    Labels: Leben einer Person (de) / person's life (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PersonLife"
