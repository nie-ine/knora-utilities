#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Convolute import Convolute
from ...information_carrier.properties.carrierHasDescription import CarrierHasDescription
from ...information_carrier.properties.convoluteHasOriginDescription import ConvoluteHasOriginDescription
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:PolyAuthorPublicationConvolute

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class PolyAuthorPublicationConvolute(Convolute):
    """
    Convolute of poems authored by Kuno Raeber as published among expressions
    by other authors.

    Labels: Mehrautorenpublikationen-Konvolut (de) / poly-author publication convolute (en)
    """
    def __init__(self, carrierHasDescription=None, convoluteHasOriginDescription=None, **kwargs):
        """

        :param carrierHasDescription:
        :param convoluteHasOriginDescription:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PolyAuthorPublicationConvolute"

        self.carrierHasDescription = CarrierHasDescription(carrierHasDescription)
        self.convoluteHasOriginDescription = ConvoluteHasOriginDescription(convoluteHasOriginDescription)
