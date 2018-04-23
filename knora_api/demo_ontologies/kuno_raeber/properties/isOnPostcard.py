#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.properties.isInManuscript import IsInManuscript

"""
definition of property kuno-raeber:IsOnPostcard

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class IsOnPostcard(IsInManuscript):
    """
    Relating a poem by Kuno Raeber to a postcard it is on.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "isOnPostcard"
