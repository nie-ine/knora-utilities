#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...concept.properties.isPartOf import IsPartOf

"""
definition of property text-structure:IsParagraphOf

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class IsParagraphOf(IsPartOf):
    """
    Relating a paragraph to a text it is part of.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-structure"
        self._name = "isParagraphOf"
