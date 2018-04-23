#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.properties.isOnPage import IsOnPage as Inf_IsOnPage

"""
definition of property kuno-raeber:IsOnPage

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class IsOnPage(Inf_IsOnPage):
    """
    Relating a handwritten poem by Kuno Raeber to a carrier page it is on.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "isOnPage"
