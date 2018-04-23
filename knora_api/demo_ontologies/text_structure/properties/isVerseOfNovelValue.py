#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .isLineOfValue import IsLineOfValue

"""
definition of property text-structure:IsVerseOfNovelValue

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class IsVerseOfNovelValue(IsLineOfValue):
    """
    Relating a verse to a reification statement of the relation between the verse and a verse novel it is part of.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-structure"
        self._name = "isVerseOfNovelValue"
