#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Space import Space
from ..properties.placeHasName import PlaceHasName
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class physical-resource:Place

created at: 2018-04-19 14:07:12
created from: physical-resource-ontology-knora.ttl
"""


class Place(Space):
    """
    Specific part of space.

    Labels: Platz (de) / place (en)
    """
    def __init__(self, placeHasName=None, **kwargs):
        """

        :param placeHasName:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Place"

        self.placeHasName = PlaceHasName(placeHasName)
