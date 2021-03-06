#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.booleanValue import BooleanValue

"""
definition of property kuno-raeber:IsInSwissGerman

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class IsInSwissGerman(BooleanValue):
    """
    Relating a text by Kuno Raeber to being expressed in Swiss German or not.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "isInSwissGerman"
