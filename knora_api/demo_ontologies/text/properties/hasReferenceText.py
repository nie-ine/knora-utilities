#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property text:HasReferenceText

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class HasReferenceText(HasLinkTo):
    """
    Relating a text to another one as its reference.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text"
        self._name = "hasReferenceText"
