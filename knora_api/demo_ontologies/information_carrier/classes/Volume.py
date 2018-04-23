#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Book import Book
from ..properties.volumeHasNumber import VolumeHasNumber
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:Volume

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class Volume(Book):
    """
    One of the books carrying an expression materialized in more than one book.

    Labels: Band (de) / volume (en)
    """
    def __init__(self, volumeHasNumber=None, **kwargs):
        """

        :param volumeHasNumber:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Volume"

        self.volumeHasNumber = VolumeHasNumber(volumeHasNumber)
