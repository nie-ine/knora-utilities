#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.properties.isOnCarrier import IsOnCarrier

"""
definition of property publishing:IsPublishedIn

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class IsPublishedIn(IsOnCarrier):
    """
    Relating a publication expression to a publication thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "isPublishedIn"
