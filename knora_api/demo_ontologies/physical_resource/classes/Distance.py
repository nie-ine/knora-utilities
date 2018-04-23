#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Length import Length
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class physical-resource:Distance

created at: 2018-04-19 14:07:12
created from: physical-resource-ontology-knora.ttl
"""


class Distance(Length):
    """
    Length of the space between two points.

    Labels: Abstand (de) / distance (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Distance"
