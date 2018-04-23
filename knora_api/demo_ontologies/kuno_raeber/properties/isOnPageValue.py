#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.properties.isOnPageValue import IsOnPageValue as Inf_IsOnPageValue

"""
definition of property kuno-raeber:IsOnPageValue

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class IsOnPageValue(Inf_IsOnPageValue):
    """
    Relating a handwritten poem by Kuno Raeber to a reification statement of the relation between the poem and a carrier page it is on.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "isOnPageValue"
