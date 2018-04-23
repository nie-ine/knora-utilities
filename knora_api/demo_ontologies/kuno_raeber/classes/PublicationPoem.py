#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...publishing.classes.Expression import Expression
from .Poem import Poem
from ..properties.isInPolyAuthorPublicationConvolute import IsInPolyAuthorPublicationConvolute
from ...publishing.properties.hasNachlassPublicationDescription import HasNachlassPublicationDescription
from ...information_carrier.properties.hasPageNumberDescription import HasPageNumberDescription
from ...publishing.properties.hasPublicationNumber import HasPublicationNumber
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:PublicationPoem

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class PublicationPoem(Expression, Poem):
    """
    Poem authored by Kuno Raeber as publication.

    Labels: Publikation-Gedicht (de) / publication poem (en)
    """
    def __init__(self, isInPolyAuthorPublicationConvolute=None, hasNachlassPublicationDescription=None, hasPageNumberDescription=None, hasPublicationNumber=None, **kwargs):
        """

        :param isInPolyAuthorPublicationConvolute:
        :param hasNachlassPublicationDescription:
        :param hasPageNumberDescription:
        :param hasPublicationNumber:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PublicationPoem"

        self.isInPolyAuthorPublicationConvolute = IsInPolyAuthorPublicationConvolute(isInPolyAuthorPublicationConvolute)
        self.hasNachlassPublicationDescription = HasNachlassPublicationDescription(hasNachlassPublicationDescription)
        self.hasPageNumberDescription = HasPageNumberDescription(hasPageNumberDescription)
        self.hasPublicationNumber = HasPublicationNumber(hasPublicationNumber)
