#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.Action import Action
from ..properties.teachingBy import TeachingBy
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class teaching:Teaching

created at: 2018-04-19 14:07:12
created from: teaching-ontology-knora.ttl
"""


class Teaching(Action):
    """
    Person's action of communicating information in order to help another
    person to acquire knowledge, competence or value.

    Labels: Unterricht (de) / teaching (en)
    """
    def __init__(self, teachingBy=None, **kwargs):
        """

        :param teachingBy:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Teaching"

        self.teachingBy = TeachingBy(teachingBy)
