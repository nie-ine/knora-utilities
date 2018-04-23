#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .isOnCarrier import IsOnCarrier

"""
definition of property information-carrier:IsInTypescript

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class IsInTypescript(IsOnCarrier):
    """
    Relating a typewritten text to the typescript that carries it.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/information-carrier"
        self._name = "isInTypescript"
