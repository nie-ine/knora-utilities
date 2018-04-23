#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .isPartOfValue import IsPartOfValue

"""
definition of property physical-resource:IsPartOfNachlassValue

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class IsPartOfNachlassValue(IsPartOfValue):
    """
    Relating an element of a nachlass to a reification statement of the relation between the element and the nachlass.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/physical-resource"
        self._name = "isPartOfNachlassValue"
