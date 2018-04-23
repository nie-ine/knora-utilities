#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasName import HasName

"""
definition of property text:HasAlias

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class HasAlias(HasName):
    """
    Relating a resource to an alias (as object) as an alternative name of the resource.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text"
        self._name = "hasAlias"
