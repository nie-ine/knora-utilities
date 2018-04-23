#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Information import Information
from ...publishing.properties.hasPolyAuthorPublication import HasPolyAuthorPublication
from ...information_carrier.properties.isOnCarrier import IsOnCarrier
from ...publishing.properties.hasPublication import HasPublication
from ...publishing.properties.isPublishedOnline import IsPublishedOnline
from ...publishing.properties.hasUnauthorizedRepublication import HasUnauthorizedRepublication
from ...publishing.properties.hasLastPublication import HasLastPublication
from ...publishing.properties.hasPublishingState import HasPublishingState
from ...publishing.properties.hasPublicationNumber import HasPublicationNumber
from ...publishing.properties.hasLastAuthorizedPublication import HasLastAuthorizedPublication
from ...publishing.properties.hasUnauthorizedPublication import HasUnauthorizedPublication
from ..properties.isPartOfCycle import IsPartOfCycle
from ..properties.hasContentSubject import HasContentSubject
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class concept:Expression

created at: 2018-04-19 14:07:12
created from: concept-ontology-knora.ttl
"""


class Expression(Information):
    """
    Identifiable immaterial realisation of an individual work, e.g. a text,
    story, poem, play, musical, song, joke, choreographic notation, movement
    pattern, sound pattern, image, multimedia object, or any combination of them,
    having an objectively recognisable structure.

    Labels: Expression (de) / expression (en)
    """
    def __init__(self, hasPolyAuthorPublication=None, isOnCarrier=None, hasPublication=None, isPublishedOnline=None, hasUnauthorizedRepublication=None, hasLastPublication=None, hasPublishingState=None, hasPublicationNumber=None, hasLastAuthorizedPublication=None, hasUnauthorizedPublication=None, isPartOfCycle=None, hasContentSubject=None, **kwargs):
        """

        :param hasPolyAuthorPublication:
        :param isOnCarrier:
        :param hasPublication:
        :param isPublishedOnline:
        :param hasUnauthorizedRepublication:
        :param hasLastPublication:
        :param hasPublishingState:
        :param hasPublicationNumber:
        :param hasLastAuthorizedPublication:
        :param hasUnauthorizedPublication:
        :param isPartOfCycle:
        :param hasContentSubject:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Expression"

        self.hasPolyAuthorPublication = HasPolyAuthorPublication(hasPolyAuthorPublication)
        self.isOnCarrier = IsOnCarrier(isOnCarrier)
        self.hasPublication = HasPublication(hasPublication)
        self.isPublishedOnline = IsPublishedOnline(isPublishedOnline)
        self.hasUnauthorizedRepublication = HasUnauthorizedRepublication(hasUnauthorizedRepublication)
        self.hasLastPublication = HasLastPublication(hasLastPublication)
        self.hasPublishingState = HasPublishingState(hasPublishingState)
        self.hasPublicationNumber = HasPublicationNumber(hasPublicationNumber)
        self.hasLastAuthorizedPublication = HasLastAuthorizedPublication(hasLastAuthorizedPublication)
        self.hasUnauthorizedPublication = HasUnauthorizedPublication(hasUnauthorizedPublication)
        self.isPartOfCycle = IsPartOfCycle(isPartOfCycle)
        self.hasContentSubject = HasContentSubject(hasContentSubject)
