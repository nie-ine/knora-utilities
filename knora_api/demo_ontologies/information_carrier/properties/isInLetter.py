#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .isOnCarrier import IsOnCarrier

"""
definition of property information-carrier:IsInLetter

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class IsInLetter(IsOnCarrier):
    """
    Relating a letter expression to a letter it is in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/information-carrier"
        self._name = "isInLetter"
