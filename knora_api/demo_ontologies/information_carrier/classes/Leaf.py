#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Carrier import Carrier
from ..properties.isLeafOf import IsLeafOf
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:Leaf

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class Leaf(Carrier):
    """
    Sheet of a writable substance, e.g. paper or parchment.

    Labels: Blatt (de) / leaf (en)
    """
    def __init__(self, isLeafOf=None, **kwargs):
        """

        :param isLeafOf:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Leaf"

        self.isLeafOf = IsLeafOf(isLeafOf)
