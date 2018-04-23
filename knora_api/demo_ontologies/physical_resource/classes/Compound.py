#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Matter import Matter
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class physical-resource:Compound

created at: 2018-04-19 14:07:12
created from: physical-resource-ontology-knora.ttl
"""


class Compound(Matter):
    """
    Physical resource composed of more than 1 type of substance.

    Labels: Mischung (de) / compound (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Compound"
