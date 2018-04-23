#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...concept.properties.isPartOf import IsPartOf

"""
definition of property text-editing:IsApparatusOf

created at: 2018-04-19 14:07:12
created from: text-editing-ontology-knora.ttl
"""


class IsApparatusOf(IsPartOf):
    """
    Relating a critical apparatus to its critical edition.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-editing"
        self._name = "isApparatusOf"
