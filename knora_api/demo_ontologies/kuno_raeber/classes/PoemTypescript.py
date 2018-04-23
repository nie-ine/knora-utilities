#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.classes.ArchiveElement import ArchiveElement
from ...information_carrier.classes.Leaf import Leaf
from ...information_carrier.classes.Typescript import Typescript
from ...information_carrier.properties.hasArchiveSignature import HasArchiveSignature
from ..properties.isPartOfTypescriptConvolute import IsPartOfTypescriptConvolute
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:PoemTypescript

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class PoemTypescript(ArchiveElement, Leaf, Typescript):
    """
    Poem typescript by Kuno Raeber.

    Labels: Gedicht-Typoskript (de) / poem typescript (en)
    """
    def __init__(self, hasArchiveSignature=None, isPartOfTypescriptConvolute=None, **kwargs):
        """

        :param hasArchiveSignature:
        :param isPartOfTypescriptConvolute:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PoemTypescript"

        self.hasArchiveSignature = HasArchiveSignature(hasArchiveSignature)
        self.isPartOfTypescriptConvolute = IsPartOfTypescriptConvolute(isPartOfTypescriptConvolute)
