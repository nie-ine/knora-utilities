#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .code import Code

"""
definition of property language:HasCode

created at: 2018-04-19 14:07:12
created from: language-ontology-knora.ttl
"""


class HasCode(Code):
    """
    Relating a language to a code (object) representing that language.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/language"
        self._name = "hasCode"
