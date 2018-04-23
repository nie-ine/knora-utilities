#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .ImageCarrier import ImageCarrier
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class image:Photograph

created at: 2018-04-19 14:07:12
created from: image-ontology-knora.ttl
"""


class Photograph(ImageCarrier):
    """
    Image made by exposing a photosensitive surface to light.

    Labels: Foto (de) / photograph (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Photograph"
