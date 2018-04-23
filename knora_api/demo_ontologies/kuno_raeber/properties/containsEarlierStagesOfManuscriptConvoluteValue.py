#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.properties.containsEarlierStagesOfValue import ContainsEarlierStagesOfValue

"""
definition of property kuno-raeber:ContainsEarlierStagesOfManuscriptConvoluteValue

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class ContainsEarlierStagesOfManuscriptConvoluteValue(ContainsEarlierStagesOfValue):
    """
    Relating a convolute to a reification statement of the relation between the convolute and another one containing manuscripts with later stages of poems by Kuno Raeber of the former convolute.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "containsEarlierStagesOfManuscriptConvoluteValue"
