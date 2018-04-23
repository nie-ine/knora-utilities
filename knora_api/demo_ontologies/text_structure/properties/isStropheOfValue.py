#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .isParagraphOfValue import IsParagraphOfValue

"""
definition of property text-structure:IsStropheOfValue

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class IsStropheOfValue(IsParagraphOfValue):
    """
    Relating a strophe to a reification statement of the relation between the strophe and a verse poem it is part of.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-structure"
        self._name = "isStropheOfValue"
