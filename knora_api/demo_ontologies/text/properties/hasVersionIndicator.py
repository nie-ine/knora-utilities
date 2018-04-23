#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasContent import HasContent

"""
definition of property text:HasVersionIndicator

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class HasVersionIndicator(HasContent):
    """
    Relating a text expression to a textual element (as object) that indicates its version.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text"
        self._name = "hasVersionIndicator"
