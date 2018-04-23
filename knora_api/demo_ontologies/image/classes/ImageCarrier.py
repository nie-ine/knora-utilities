#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.classes.Carrier import Carrier
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class image:ImageCarrier

created at: 2018-04-19 14:07:12
created from: image-ontology-knora.ttl
"""


class ImageCarrier(Carrier):
    """
    Visual representation of a resource on a carrier.

    Labels: Bildträger (de) / image carrier (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "ImageCarrier"
