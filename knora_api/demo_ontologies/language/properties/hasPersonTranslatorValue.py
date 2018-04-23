#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasTranslatorValue import HasTranslatorValue

"""
definition of property language:HasPersonTranslatorValue

created at: 2018-04-19 14:07:12
created from: language-ontology-knora.ttl
"""


class HasPersonTranslatorValue(HasTranslatorValue):
    """
    Relating a natural language expression to a reification statement of the relation between the expression and a person who translated it.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/language"
        self._name = "hasPersonTranslatorValue"
