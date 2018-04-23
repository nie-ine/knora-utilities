#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasDescription import HasDescription

"""
definition of property text:HasDefinition

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class HasDefinition(HasDescription):
    """
    Relating a resource to a definition (as object) as a textual statement about the essential features of the resource.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text"
        self._name = "hasDefinition"
