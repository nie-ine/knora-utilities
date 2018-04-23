#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...physical_resource.properties.isPartOfValue import IsPartOfValue

"""
definition of property kuno-raeber:IsPartOfLetterConvoluteValue

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class IsPartOfLetterConvoluteValue(IsPartOfValue):
    """
    Relating a letter by Kuno Raeber to a reification statement of the relation between the letter and a convolute it is in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "isPartOfLetterConvoluteValue"
