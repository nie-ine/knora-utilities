#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text_editing.properties.hasDiplomaticTranscription import HasDiplomaticTranscription as Tex_HasDiplomaticTranscription

"""
definition of property kuno-raeber:HasDiplomaticTranscription

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class HasDiplomaticTranscription(Tex_HasDiplomaticTranscription):
    """
    Relating a handwritten poem by Kuno Raeber to a diplomatic transcription thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "hasDiplomaticTranscription"
