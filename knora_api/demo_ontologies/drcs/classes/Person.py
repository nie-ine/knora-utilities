#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.Person import Person as hum_Person
from ...human.properties.hasName import HasName
from ..properties.hasStegmuellerPersonDescription import HasStegmuellerPersonDescription
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class drcs:Person

created at: 2018-04-19 14:07:12
created from: drcs-ontology-knora.ttl
"""


class Person(hum_Person):
    """
    Person as subject in the scientific study of Petrus Lombardus.

    Labels: Person (de) / person (en) / personne (fr) / persona (it)
    """
    def __init__(self, hasName=None, hasStegmuellerPersonDescription=None, **kwargs):
        """

        :param hasName:
        :param hasStegmuellerPersonDescription:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Person"

        self.hasName = HasName(hasName)
        self.hasStegmuellerPersonDescription = HasStegmuellerPersonDescription(hasStegmuellerPersonDescription)
