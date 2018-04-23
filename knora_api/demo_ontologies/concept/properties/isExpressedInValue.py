#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property concept:IsExpressedInValue

created at: 2018-04-19 14:07:12
created from: concept-ontology-knora.ttl
"""


class IsExpressedInValue(HasLinkToValue):
    """
    Relating a work to a reification statement of the relation between the work and an expression thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/concept"
        self._name = "isExpressedInValue"
