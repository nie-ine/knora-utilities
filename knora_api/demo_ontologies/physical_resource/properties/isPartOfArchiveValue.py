#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .isPartOfValue import IsPartOfValue

"""
definition of property physical-resource:IsPartOfArchiveValue

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class IsPartOfArchiveValue(IsPartOfValue):
    """
    Relating an element of an archive to a reification statement of the relation between the element and the archive.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/physical-resource"
        self._name = "isPartOfArchiveValue"
