#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Space import Space
from ..properties.hasLength import HasLength
from ..properties.hasSize import HasSize
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class physical-resource:Matter

created at: 2018-04-19 14:07:12
created from: physical-resource-ontology-knora.ttl
"""


class Matter(Space):
    """
    Physical resource having mass and volume.

    Labels: Materie (de) / matter (en)
    """
    def __init__(self, hasLength=None, hasSize=None, **kwargs):
        """

        :param hasLength:
        :param hasSize:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Matter"

        self.hasLength = HasLength(hasLength)
        self.hasSize = HasSize(hasSize)
