#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...physical_resource.properties.isPartOf import IsPartOf

"""
definition of property kuno-raeber:IsPartOfLetterConvolute

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class IsPartOfLetterConvolute(IsPartOf):
    """
    Relating a letter by Kuno Raeber to a convolute it is in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "isPartOfLetterConvolute"
