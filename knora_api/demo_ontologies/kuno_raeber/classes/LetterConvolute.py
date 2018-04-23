#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.classes.ArchiveElement import ArchiveElement
from .Convolute import Convolute
from ...information_carrier.properties.convoluteHasContentRepresentation import ConvoluteHasContentRepresentation
from ...information_carrier.properties.hasArchiveSignature import HasArchiveSignature
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:LetterConvolute

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class LetterConvolute(ArchiveElement, Convolute):
    """
    Convolute of letters written by and to Kuno Raeber.

    Labels: Briefekonvolut (de) / letter convolute (en)
    """
    def __init__(self, convoluteHasContentRepresentation=None, hasArchiveSignature=None, **kwargs):
        """

        :param convoluteHasContentRepresentation:
        :param hasArchiveSignature:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "LetterConvolute"

        self.convoluteHasContentRepresentation = ConvoluteHasContentRepresentation(convoluteHasContentRepresentation)
        self.hasArchiveSignature = HasArchiveSignature(hasArchiveSignature)
