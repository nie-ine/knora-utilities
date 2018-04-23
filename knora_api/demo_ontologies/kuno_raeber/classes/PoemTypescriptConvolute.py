#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.classes.ArchiveElement import ArchiveElement
from .Convolute import Convolute
from ...information_carrier.properties.containsEarlierStagesOfPublication import ContainsEarlierStagesOfPublication
from ...information_carrier.properties.convoluteHasContentRepresentation import ConvoluteHasContentRepresentation
from ..properties.containsLaterStagesOfManuscriptConvolute import ContainsLaterStagesOfManuscriptConvolute
from ...information_carrier.properties.hasArchiveSignature import HasArchiveSignature
from ...information_carrier.properties.convoluteHasOriginDescription import ConvoluteHasOriginDescription
from ...information_carrier.properties.hasCarrierCollectionDescription import HasCarrierCollectionDescription
from ..properties.containsLaterStagesOfNotebook import ContainsLaterStagesOfNotebook
from ...information_carrier.properties.convoluteHasSizeDescription import ConvoluteHasSizeDescription
from ...human.properties.hasCreating import HasCreating
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:PoemTypescriptConvolute

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class PoemTypescriptConvolute(ArchiveElement, Convolute):
    """
    Poem typescript convolute with poems authored by Kuno Raeber.

    Labels: Gedicht-Typoskriptenonvolut (de) / poem typescript convolute (en)
    """
    def __init__(self, containsEarlierStagesOfPublication=None, convoluteHasContentRepresentation=None, containsLaterStagesOfManuscriptConvolute=None, hasArchiveSignature=None, convoluteHasOriginDescription=None, hasCarrierCollectionDescription=None, containsLaterStagesOfNotebook=None, convoluteHasSizeDescription=None, hasCreating=None, **kwargs):
        """

        :param containsEarlierStagesOfPublication:
        :param convoluteHasContentRepresentation:
        :param containsLaterStagesOfManuscriptConvolute:
        :param hasArchiveSignature:
        :param convoluteHasOriginDescription:
        :param hasCarrierCollectionDescription:
        :param containsLaterStagesOfNotebook:
        :param convoluteHasSizeDescription:
        :param hasCreating:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PoemTypescriptConvolute"

        self.containsEarlierStagesOfPublication = ContainsEarlierStagesOfPublication(containsEarlierStagesOfPublication)
        self.convoluteHasContentRepresentation = ConvoluteHasContentRepresentation(convoluteHasContentRepresentation)
        self.containsLaterStagesOfManuscriptConvolute = ContainsLaterStagesOfManuscriptConvolute(containsLaterStagesOfManuscriptConvolute)
        self.hasArchiveSignature = HasArchiveSignature(hasArchiveSignature)
        self.convoluteHasOriginDescription = ConvoluteHasOriginDescription(convoluteHasOriginDescription)
        self.hasCarrierCollectionDescription = HasCarrierCollectionDescription(hasCarrierCollectionDescription)
        self.containsLaterStagesOfNotebook = ContainsLaterStagesOfNotebook(containsLaterStagesOfNotebook)
        self.convoluteHasSizeDescription = ConvoluteHasSizeDescription(convoluteHasSizeDescription)
        self.hasCreating = HasCreating(hasCreating)
