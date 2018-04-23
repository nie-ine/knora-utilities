#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.PhysicalCreation import PhysicalCreation
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:Nachlass

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class Nachlass(PhysicalCreation):
    """
    Collection of materialized expressions of a person as existing after the
    person's death.

    Labels: Nachlass (de) / nachlass (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Nachlass"
