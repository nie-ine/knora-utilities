#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .PoemTypescriptConvolute import PoemTypescriptConvolute
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:PoemTypescriptConvoluteWithImage

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class PoemTypescriptConvoluteWithImage(PoemTypescriptConvolute):
    """
    Poem typescript convolute with poems authored by Kuno Raeber, mit bild.

    Labels: Gedicht-Typoskriptenonvolut mit Bild (de) / poem typescript convolute with image (en)
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PoemTypescriptConvoluteWithImage"
