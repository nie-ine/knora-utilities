#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .isOnCarrierValue import IsOnCarrierValue

"""
definition of property information-carrier:IsInDiaryValue

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class IsInDiaryValue(IsOnCarrierValue):
    """
    Relating a diary entry to a reification statement of the relation between the diary entry and a diary it is in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/information-carrier"
        self._name = "isInDiaryValue"
