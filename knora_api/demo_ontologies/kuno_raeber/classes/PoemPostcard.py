#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.classes.Postcard import Postcard
from ...information_carrier.classes.Manuscript import Manuscript
from ...information_carrier.properties.hasArchiveSignature import HasArchiveSignature
from ..properties.isPartOfPostcardConvolute import IsPartOfPostcardConvolute
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:PoemPostcard

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class PoemPostcard(Postcard, Manuscript):
    """
    Postcard with a poem authored by Kuno Raeber.

    Labels: Gedicht-Postkarte (de) / poem postcard (en)
    """
    def __init__(self, hasArchiveSignature=None, isPartOfPostcardConvolute=None, **kwargs):
        """

        :param hasArchiveSignature:
        :param isPartOfPostcardConvolute:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PoemPostcard"

        self.hasArchiveSignature = HasArchiveSignature(hasArchiveSignature)
        self.isPartOfPostcardConvolute = IsPartOfPostcardConvolute(isPartOfPostcardConvolute)
