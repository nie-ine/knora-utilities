#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.properties.isInDiaryValue import IsInDiaryValue as Inf_IsInDiaryValue

"""
definition of property kuno-raeber:IsInDiaryValue

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class IsInDiaryValue(Inf_IsInDiaryValue):
    """
    Relating a diary entry by Kuno Raeber to a reification statement of the relation between the diary entry and the diary it is in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "isInDiaryValue"
