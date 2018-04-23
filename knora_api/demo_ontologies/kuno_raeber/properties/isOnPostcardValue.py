#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.properties.isInManuscriptValue import IsInManuscriptValue

"""
definition of property kuno-raeber:IsOnPostcardValue

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class IsOnPostcardValue(IsInManuscriptValue):
    """
    Relating a poem by Kuno Raeber to a reification statement of the relation between the poem and a postcard it is on.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "isOnPostcardValue"
