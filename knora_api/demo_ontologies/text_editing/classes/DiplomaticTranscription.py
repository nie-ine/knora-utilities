#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .Derivative import Derivative
from ..properties.isDiplomaticTranscriptionOfTextOnPage import IsDiplomaticTranscriptionOfTextOnPage
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class text-editing:DiplomaticTranscription

created at: 2018-04-19 14:07:12
created from: text-editing-ontology-knora.ttl
"""


class DiplomaticTranscription(Derivative):
    """
    Transcription of a text with diacritical signs indicating visual textual
    properties to describe the textual state.

    Labels: diplomatische Umschrift (de) / diplomatic transcription (en)
    """
    def __init__(self, isDiplomaticTranscriptionOfTextOnPage=None, **kwargs):
        """

        :param isDiplomaticTranscriptionOfTextOnPage:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "DiplomaticTranscription"

        self.isDiplomaticTranscriptionOfTextOnPage = IsDiplomaticTranscriptionOfTextOnPage(isDiplomaticTranscriptionOfTextOnPage)
