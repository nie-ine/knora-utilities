#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.properties.isOnCarrierValue import IsOnCarrierValue

"""
definition of property publishing:IsPublishedInValue

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class IsPublishedInValue(IsOnCarrierValue):
    """
    Relating a publication expression to a reification statement of the relation between the publication expression and a publication thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "isPublishedInValue"
