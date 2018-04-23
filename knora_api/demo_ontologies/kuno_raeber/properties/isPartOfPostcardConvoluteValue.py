#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...physical_resource.properties.isPartOfValue import IsPartOfValue

"""
definition of property kuno-raeber:IsPartOfPostcardConvoluteValue

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class IsPartOfPostcardConvoluteValue(IsPartOfValue):
    """
    Relating a poem postcard by Kuno Raeber to a reification statement of the relation between the poem postcard and the convolute it is part of.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "isPartOfPostcardConvoluteValue"
