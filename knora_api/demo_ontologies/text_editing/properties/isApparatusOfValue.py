#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...concept.properties.isPartOfValue import IsPartOfValue

"""
definition of property text-editing:IsApparatusOfValue

created at: 2018-04-19 14:07:12
created from: text-editing-ontology-knora.ttl
"""


class IsApparatusOfValue(IsPartOfValue):
    """
    Relating a critical apparatus to a reification statement of the relation between the apparatus and its critical edition.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-editing"
        self._name = "isApparatusOfValue"
