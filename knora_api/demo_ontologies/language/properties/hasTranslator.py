#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property language:HasTranslator

created at: 2018-04-19 14:07:12
created from: language-ontology-knora.ttl
"""


class HasTranslator(HasLinkTo):
    """
    Relating a natural language expression to an agent that translated it.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/language"
        self._name = "hasTranslator"
