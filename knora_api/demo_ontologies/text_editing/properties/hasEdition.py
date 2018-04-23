#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property text-editing:HasEdition

created at: 2018-04-19 14:07:12
created from: text-editing-ontology-knora.ttl
"""


class HasEdition(HasLinkTo):
    """
    Relating a text to an edition thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-editing"
        self._name = "hasEdition"
