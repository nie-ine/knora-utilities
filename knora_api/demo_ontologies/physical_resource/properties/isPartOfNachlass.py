#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .isPartOf import IsPartOf

"""
definition of property physical-resource:IsPartOfNachlass

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class IsPartOfNachlass(IsPartOf):
    """
    Relating an element of a nachlass to the nachlass.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/physical-resource"
        self._name = "isPartOfNachlass"
