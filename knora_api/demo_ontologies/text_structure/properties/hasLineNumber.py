#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasContent import HasContent

"""
definition of property text-structure:HasLineNumber

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class HasLineNumber(HasContent):
    """
    Relating a text expression to the number (as object) of a line thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-structure"
        self._name = "hasLineNumber"
