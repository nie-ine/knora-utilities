#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasName import HasName

"""
definition of property text:HasPreferredName

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class HasPreferredName(HasName):
    """
    Relating a resource to a preferred name (as object).
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text"
        self._name = "hasPreferredName"
