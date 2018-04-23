#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text_editing.classes.DiplomaticTranscription import DiplomaticTranscription as tex_DiplomaticTranscription
from ...text.properties.hasContent import HasContent
from ...knora_base.properties.seqnum import Seqnum
from ...text_editing.properties.isDiplomaticTranscriptionOfTextOnPage import IsDiplomaticTranscriptionOfTextOnPage
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class kuno-raeber:DiplomaticTranscription

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class DiplomaticTranscription(tex_DiplomaticTranscription):
    """
    Diplomatische Umschrift eines von Kuno Raeber verfassten Texts.

    Labels: diplomatische Umschrift (de) / diplomatic transcription (en)
    """
    def __init__(self, hasContent=None, seqnum=None, isDiplomaticTranscriptionOfTextOnPage=None, **kwargs):
        """

        :param hasContent:
        :param seqnum:
        :param isDiplomaticTranscriptionOfTextOnPage:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "DiplomaticTranscription"

        self.hasContent = HasContent(hasContent)
        self.seqnum = Seqnum(seqnum)
        self.isDiplomaticTranscriptionOfTextOnPage = IsDiplomaticTranscriptionOfTextOnPage(isDiplomaticTranscriptionOfTextOnPage)
