#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.properties.isOnCarrier import IsOnCarrier

"""
definition of property publishing:HasPublication

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class HasPublication(IsOnCarrier):
    """
    Relating an expression to a publication thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "hasPublication"
