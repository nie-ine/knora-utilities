#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...physical_resource.properties.isPartOfValue import IsPartOfValue

"""
definition of property kuno-raeber:IsPartOfTypescriptConvoluteValue

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class IsPartOfTypescriptConvoluteValue(IsPartOfValue):
    """
    Relating a poem typescript by Kuno Raeber to a reification statement of the relation between the poem typescript and the convolute it is part of.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "isPartOfTypescriptConvoluteValue"
