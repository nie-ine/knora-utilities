#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.Person import Person
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class organisation:ReligiousPerson

created at: 2018-04-19 14:07:12
created from: organisation-ontology-knora.ttl
"""


class ReligiousPerson(Person):
    """
    Person having religious faith or believing.

    Labels: religiöse Person (de) / religious person (en) / personne réligieuse (fr)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "ReligiousPerson"
