#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Creation import Creation
from ...physical_resource.classes.Matter import Matter
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class human:PhysicalCreation

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class PhysicalCreation(Creation, Matter):
    """
    Person's creation as physical resource.

    Labels: physische Kreation einer Person (de) / person's physical creation (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PhysicalCreation"
