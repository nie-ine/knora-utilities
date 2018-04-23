#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property concept:IsPartOfValue

created at: 2018-04-19 14:07:12
created from: concept-ontology-knora.ttl
"""


class IsPartOfValue(HasLinkToValue):
    """
    Relating something to a reification statement of the relation between that something and something else it is part of.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/concept"
        self._name = "isPartOfValue"
