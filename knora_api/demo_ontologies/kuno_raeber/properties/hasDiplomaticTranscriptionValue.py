#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text_editing.properties.hasDiplomaticTranscriptionValue import HasDiplomaticTranscriptionValue as Tex_HasDiplomaticTranscriptionValue

"""
definition of property kuno-raeber:HasDiplomaticTranscriptionValue

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class HasDiplomaticTranscriptionValue(Tex_HasDiplomaticTranscriptionValue):
    """
    Relating a poem by Kuno Raeber to a reification statement of the relation between the poem and a diplomatic transcription thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "hasDiplomaticTranscriptionValue"
