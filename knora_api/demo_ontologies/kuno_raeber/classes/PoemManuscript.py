#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.classes.ArchiveElement import ArchiveElement
from ...information_carrier.classes.Leaf import Leaf
from ...information_carrier.classes.Manuscript import Manuscript
from ...information_carrier.properties.hasArchiveSignature import HasArchiveSignature
from ..properties.isPartOfManuscriptConvolute import IsPartOfManuscriptConvolute
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:PoemManuscript

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class PoemManuscript(ArchiveElement, Leaf, Manuscript):
    """
    Manuscript with a poem authored by Kuno Raeber.

    Labels: Gedicht-Manuskript (de) / poem manuscript (en)
    """
    def __init__(self, hasArchiveSignature=None, isPartOfManuscriptConvolute=None, **kwargs):
        """

        :param hasArchiveSignature:
        :param isPartOfManuscriptConvolute:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PoemManuscript"

        self.hasArchiveSignature = HasArchiveSignature(hasArchiveSignature)
        self.isPartOfManuscriptConvolute = IsPartOfManuscriptConvolute(isPartOfManuscriptConvolute)
