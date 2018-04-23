#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Pen import Pen
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:FountainPen

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class FountainPen(Pen):
    """
    Pen with refillable reservoir for fluid ink for feeding a metal nib.

    Labels: Füller (de) / fountain pen (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "FountainPen"
