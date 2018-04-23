#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property language:ExpressedInNaturalLanguage

created at: 2018-04-19 14:07:12
created from: language-ontology-knora.ttl
"""


class ExpressedInNaturalLanguage(HasLinkTo):
    """
    Relating a human expression to a natural language wherein it is expressed.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/language"
        self._name = "expressedInNaturalLanguage"
