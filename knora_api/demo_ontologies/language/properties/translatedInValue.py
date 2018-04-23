#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property language:TranslatedInValue

created at: 2018-04-19 14:07:12
created from: language-ontology-knora.ttl
"""


class TranslatedInValue(HasLinkToValue):
    """
    Relating a human natural language expression to a reification statement of the relation between the expression and another one in another natural language it is translated in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/language"
        self._name = "translatedInValue"
