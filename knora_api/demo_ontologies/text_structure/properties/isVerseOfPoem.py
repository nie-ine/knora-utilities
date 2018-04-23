#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .isVerseOf import IsVerseOf
from .isLineOf import IsLineOf

"""
definition of property text-structure:IsVerseOfPoem

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class IsVerseOfPoem(IsVerseOf,IsLineOf):
    """
    Relating a verse to a verse poem it is part of.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-structure"
        self._name = "isVerseOfPoem"
