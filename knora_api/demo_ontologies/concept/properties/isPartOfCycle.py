#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .isPartOf import IsPartOf

"""
definition of property concept:IsPartOfCycle

created at: 2018-04-19 14:07:12
created from: concept-ontology-knora.ttl
"""


class IsPartOfCycle(IsPartOf):
    """
    Relating an expression to a cycle it is part of.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/concept"
        self._name = "isPartOfCycle"
