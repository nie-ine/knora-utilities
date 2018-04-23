#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...concept.properties.isPartOfValue import IsPartOfValue

"""
definition of property text-structure:IsLineOfValue

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class IsLineOfValue(IsPartOfValue):
    """
    Relating a text line to a reification statement of the relation between the line and a text it is part of.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-structure"
        self._name = "isLineOfValue"
