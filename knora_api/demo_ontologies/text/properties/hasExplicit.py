#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasText import HasText

"""
definition of property text:HasExplicit

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class HasExplicit(HasText):
    """
    Relating an untitled text expression to an end part thereof (as object) to identify the text.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text"
        self._name = "hasExplicit"
