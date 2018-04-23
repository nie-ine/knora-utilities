#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.classes.Creation import Creation
from ..properties.containsEarlierStagesOf import ContainsEarlierStagesOf
from ..properties.convoluteHasTitle import ConvoluteHasTitle
from ..properties.convoluteHasDescription import ConvoluteHasDescription
from ..properties.containsEarlierStagesOfPublication import ContainsEarlierStagesOfPublication
from ..properties.convoluteHasContentRepresentation import ConvoluteHasContentRepresentation
from ..properties.convoluteHasOriginDescription import ConvoluteHasOriginDescription
from ..properties.hasCarrierCollectionDescription import HasCarrierCollectionDescription
from ..properties.convoluteHasSizeDescription import ConvoluteHasSizeDescription
from ..properties.containsLaterStagesOf import ContainsLaterStagesOf
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class information-carrier:Convolute

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class Convolute(Creation):
    """
    information carriers, e.g. of drafts, manuscripts, typoscripts or prints,
    gathered as one.

    Labels: Konvolut (de) / convolute (en)
    """
    def __init__(self, containsEarlierStagesOf=None, convoluteHasTitle=None, convoluteHasDescription=None, containsEarlierStagesOfPublication=None, convoluteHasContentRepresentation=None, convoluteHasOriginDescription=None, hasCarrierCollectionDescription=None, convoluteHasSizeDescription=None, containsLaterStagesOf=None, **kwargs):
        """

        :param containsEarlierStagesOf:
        :param convoluteHasTitle:
        :param convoluteHasDescription:
        :param containsEarlierStagesOfPublication:
        :param convoluteHasContentRepresentation:
        :param convoluteHasOriginDescription:
        :param hasCarrierCollectionDescription:
        :param convoluteHasSizeDescription:
        :param containsLaterStagesOf:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Convolute"

        self.containsEarlierStagesOf = ContainsEarlierStagesOf(containsEarlierStagesOf)
        self.convoluteHasTitle = ConvoluteHasTitle(convoluteHasTitle)
        self.convoluteHasDescription = ConvoluteHasDescription(convoluteHasDescription)
        self.containsEarlierStagesOfPublication = ContainsEarlierStagesOfPublication(containsEarlierStagesOfPublication)
        self.convoluteHasContentRepresentation = ConvoluteHasContentRepresentation(convoluteHasContentRepresentation)
        self.convoluteHasOriginDescription = ConvoluteHasOriginDescription(convoluteHasOriginDescription)
        self.hasCarrierCollectionDescription = HasCarrierCollectionDescription(hasCarrierCollectionDescription)
        self.convoluteHasSizeDescription = ConvoluteHasSizeDescription(convoluteHasSizeDescription)
        self.containsLaterStagesOf = ContainsLaterStagesOf(containsLaterStagesOf)
