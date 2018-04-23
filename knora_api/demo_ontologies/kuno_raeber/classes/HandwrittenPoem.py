#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Poem import Poem
from ...text.classes.HandwrittenText import HandwrittenText
from ..properties.hasDiplomaticTranscription import HasDiplomaticTranscription
from ...information_carrier.properties.hasPageNumberDescription import HasPageNumberDescription
from ..properties.isOnPage import IsOnPage
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:HandwrittenPoem

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class HandwrittenPoem(Poem, HandwrittenText):
    """
    Handgeschriebenes Gedicht von Kuno Raeber.

    Labels: handgeschriebenes Gedicht (de) / handwritten poem (en)
    """
    def __init__(self, hasDiplomaticTranscription=None, hasPageNumberDescription=None, isOnPage=None, **kwargs):
        """

        :param hasDiplomaticTranscription:
        :param hasPageNumberDescription:
        :param isOnPage:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "HandwrittenPoem"

        self.hasDiplomaticTranscription = HasDiplomaticTranscription(hasDiplomaticTranscription)
        self.hasPageNumberDescription = HasPageNumberDescription(hasPageNumberDescription)
        self.isOnPage = IsOnPage(isOnPage)
