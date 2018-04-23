#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...physical_resource.properties.isPartOf import IsPartOf

"""
definition of property kuno-raeber:IsPartOfManuscriptConvolute

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class IsPartOfManuscriptConvolute(IsPartOf):
    """
    Relating a poem manuscript by Kuno Raeber to the convolute it is part of.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "isPartOfManuscriptConvolute"
