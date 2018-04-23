#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Resource import Resource
from ..properties.isPartOf import IsPartOf
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class physical-resource:Space

created at: 2018-04-19 14:07:12
created from: physical-resource-ontology-knora.ttl
"""


class Space(Resource):
    """
    .

    Labels: Raum (de) / space (en)
    """
    def __init__(self, isPartOf=None, **kwargs):
        """

        :param isPartOf:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Space"

        self.isPartOf = IsPartOf(isPartOf)
