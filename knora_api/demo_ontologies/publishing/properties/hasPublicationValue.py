#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.properties.isOnCarrierValue import IsOnCarrierValue

"""
definition of property publishing:HasPublicationValue

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class HasPublicationValue(IsOnCarrierValue):
    """
    Relating an expression to a reification statement of the relation between the expression and a publication thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "hasPublicationValue"
