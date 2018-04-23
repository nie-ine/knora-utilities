#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Poem import Poem
from ...text.classes.HandwrittenText import HandwrittenText
from ..properties.hasDiplomaticTranscription import HasDiplomaticTranscription
from ..properties.isOnPostcard import IsOnPostcard
from ...publishing.properties.hasNachlassPublicationDescription import HasNachlassPublicationDescription
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:PostCardPoem

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class PostCardPoem(Poem, HandwrittenText):
    """
    Postcard poem authored by Kuno Raeber.

    Labels: Postkarten-Gedicht (de) / postcard poem (en)
    """
    def __init__(self, hasDiplomaticTranscription=None, isOnPostcard=None, hasNachlassPublicationDescription=None, **kwargs):
        """

        :param hasDiplomaticTranscription:
        :param isOnPostcard:
        :param hasNachlassPublicationDescription:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "PostCardPoem"

        self.hasDiplomaticTranscription = HasDiplomaticTranscription(hasDiplomaticTranscription)
        self.isOnPostcard = IsOnPostcard(isOnPostcard)
        self.hasNachlassPublicationDescription = HasNachlassPublicationDescription(hasNachlassPublicationDescription)
