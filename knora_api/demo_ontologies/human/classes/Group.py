#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...agent.classes.Group import Group as age_Group
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class human:Group

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class Group(age_Group):
    """
    Group of persons.

    Labels: Personengruppe (de) / group of persons (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Group"
