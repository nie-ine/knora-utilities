#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Convolute import Convolute
from ...information_carrier.properties.containsEarlierStagesOfPublication import ContainsEarlierStagesOfPublication
from ...information_carrier.properties.convoluteHasContentRepresentation import ConvoluteHasContentRepresentation
from ...information_carrier.properties.convoluteHasOriginDescription import ConvoluteHasOriginDescription
from ...information_carrier.properties.hasCarrierCollectionDescription import HasCarrierCollectionDescription
from ..properties.containsLaterStagesOfNotebook import ContainsLaterStagesOfNotebook
from ...information_carrier.properties.convoluteHasSizeDescription import ConvoluteHasSizeDescription
from ...human.properties.hasCreating import HasCreating
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:PoemPostcardConvolute

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class PoemPostcardConvolute(Convolute):
    """
    Poem postcard convolute with poems authored by Kuno Raeber.

    Labels: Gedicht-Postkartenkonvolut (de) / poem postcard convolute (en)
    """
    def __init__(self, containsEarlierStagesOfPublication=None, convoluteHasContentRepresentation=None, convoluteHasOriginDescription=None, hasCarrierCollectionDescription=None, containsLaterStagesOfNotebook=None, convoluteHasSizeDescription=None, hasCreating=None, **kwargs):
        """

        :param containsEarlierStagesOfPublication:
        :param convoluteHasContentRepresentation:
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
        self._name = "PoemPostcardConvolute"

        self.containsEarlierStagesOfPublication = ContainsEarlierStagesOfPublication(containsEarlierStagesOfPublication)
        self.convoluteHasContentRepresentation = ConvoluteHasContentRepresentation(convoluteHasContentRepresentation)
        self.convoluteHasOriginDescription = ConvoluteHasOriginDescription(convoluteHasOriginDescription)
        self.hasCarrierCollectionDescription = HasCarrierCollectionDescription(hasCarrierCollectionDescription)
        self.containsLaterStagesOfNotebook = ContainsLaterStagesOfNotebook(containsLaterStagesOfNotebook)
        self.convoluteHasSizeDescription = ConvoluteHasSizeDescription(convoluteHasSizeDescription)
        self.hasCreating = HasCreating(hasCreating)
