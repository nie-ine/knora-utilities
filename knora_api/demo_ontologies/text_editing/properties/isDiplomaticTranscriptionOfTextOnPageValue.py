#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property text-editing:IsDiplomaticTranscriptionOfTextOnPageValue

created at: 2018-04-19 14:07:12
created from: text-editing-ontology-knora.ttl
"""


class IsDiplomaticTranscriptionOfTextOnPageValue(HasLinkToValue):
    """
    Relating a diplomatic transcription to a reification statement of the relation between the diplomatic transcription and a page its source text is on.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-editing"
        self._name = "isDiplomaticTranscriptionOfTextOnPageValue"
