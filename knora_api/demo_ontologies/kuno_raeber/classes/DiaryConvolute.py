#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.classes.ArchiveElement import ArchiveElement
from .Convolute import Convolute
from ...information_carrier.properties.convoluteHasContentRepresentation import ConvoluteHasContentRepresentation
from ...information_carrier.properties.convoluteHasSizeDescription import ConvoluteHasSizeDescription
from ...information_carrier.properties.hasArchiveSignature import HasArchiveSignature
from ...human.properties.hasCreating import HasCreating
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:DiaryConvolute

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class DiaryConvolute(ArchiveElement, Convolute):
    """
    Convolute of diaries with entries authored by Kuno Raeber.

    Labels: Tagebuch-Konvolut (de) / diary convolute (en)
    """
    def __init__(self, convoluteHasContentRepresentation=None, convoluteHasSizeDescription=None, hasArchiveSignature=None, hasCreating=None, **kwargs):
        """

        :param convoluteHasContentRepresentation:
        :param convoluteHasSizeDescription:
        :param hasArchiveSignature:
        :param hasCreating:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "DiaryConvolute"

        self.convoluteHasContentRepresentation = ConvoluteHasContentRepresentation(convoluteHasContentRepresentation)
        self.convoluteHasSizeDescription = ConvoluteHasSizeDescription(convoluteHasSizeDescription)
        self.hasArchiveSignature = HasArchiveSignature(hasArchiveSignature)
        self.hasCreating = HasCreating(hasCreating)
