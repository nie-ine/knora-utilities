#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property text-editing:HasDiplomaticTranscription

created at: 2018-04-19 14:07:12
created from: text-editing-ontology-knora.ttl
"""


class HasDiplomaticTranscription(HasLinkTo):
    """
    Relating a text to a diplomatic transcription thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-editing"
        self._name = "hasDiplomaticTranscription"
