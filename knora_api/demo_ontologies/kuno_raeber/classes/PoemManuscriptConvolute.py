#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.classes.ArchiveElement import ArchiveElement
from .Convolute import Convolute
from ..properties.containsEarlierStagesOfTypescriptConvolute import ContainsEarlierStagesOfTypescriptConvolute
from ...information_carrier.properties.containsEarlierStagesOfPublication import ContainsEarlierStagesOfPublication
from ...information_carrier.properties.convoluteHasContentRepresentation import ConvoluteHasContentRepresentation
from ...information_carrier.properties.hasArchiveSignature import HasArchiveSignature
from ...information_carrier.properties.hasCarrierCollectionDescription import HasCarrierCollectionDescription
from ..properties.containsLaterStagesOfNotebook import ContainsLaterStagesOfNotebook
from ...information_carrier.properties.convoluteHasSizeDescription import ConvoluteHasSizeDescription
from ...human.properties.hasCreating import HasCreating
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:PoemManuscriptConvolute

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class PoemManuscriptConvolute(ArchiveElement, Convolute):
    """
    Poem manuscript convolute with poems authored by Kuno Raeber.

    Labels: Gedicht-Manuskriptenkonvolut (de) / poem manuscript convolute (en)
    """
    def __init__(self, containsEarlierStagesOfTypescriptConvolute=None, containsEarlierStagesOfPublication=None, convoluteHasContentRepresentation=None, hasArchiveSignature=None, hasCarrierCollectionDescription=None, containsLaterStagesOfNotebook=None, convoluteHasSizeDescription=None, hasCreating=None, **kwargs):
        """

        :param containsEarlierStagesOfTypescriptConvolute:
        :param containsEarlierStagesOfPublication:
        :param convoluteHasContentRepresentation:
        :param hasArchiveSignature:
        :param hasCarrierCollectionDescription:
        :param containsLaterStagesOfNotebook:
        :param convoluteHasSizeDescription:
        :param hasCreating:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PoemManuscriptConvolute"

        self.containsEarlierStagesOfTypescriptConvolute = ContainsEarlierStagesOfTypescriptConvolute(containsEarlierStagesOfTypescriptConvolute)
        self.containsEarlierStagesOfPublication = ContainsEarlierStagesOfPublication(containsEarlierStagesOfPublication)
        self.convoluteHasContentRepresentation = ConvoluteHasContentRepresentation(convoluteHasContentRepresentation)
        self.hasArchiveSignature = HasArchiveSignature(hasArchiveSignature)
        self.hasCarrierCollectionDescription = HasCarrierCollectionDescription(hasCarrierCollectionDescription)
        self.containsLaterStagesOfNotebook = ContainsLaterStagesOfNotebook(containsLaterStagesOfNotebook)
        self.convoluteHasSizeDescription = ConvoluteHasSizeDescription(convoluteHasSizeDescription)
        self.hasCreating = HasCreating(hasCreating)
