#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasTranslator import HasTranslator

"""
definition of property language:HasPersonTranslator

created at: 2018-04-19 14:07:12
created from: language-ontology-knora.ttl
"""


class HasPersonTranslator(HasTranslator):
    """
    Relating a natural language expression to a person who translated it.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/language"
        self._name = "hasPersonTranslator"
