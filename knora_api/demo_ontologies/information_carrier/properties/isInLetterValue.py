#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .isOnCarrierValue import IsOnCarrierValue

"""
definition of property information-carrier:IsInLetterValue

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class IsInLetterValue(IsOnCarrierValue):
    """
    Relating a letter expression to a reification statement of the relation between the letter expression and a letter it is in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/information-carrier"
        self._name = "isInLetterValue"
