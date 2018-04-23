#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasText import HasText

"""
definition of property text:HasIdentifier

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class HasIdentifier(HasText):
    """
    Relating a resource to an identifier (as object) as a unique textual reference to the resource within a given context, and conforming to a formal identification system.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text"
        self._name = "hasIdentifier"
