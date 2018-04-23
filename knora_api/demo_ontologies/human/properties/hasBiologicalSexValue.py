#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property human:HasBiologicalSexValue

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class HasBiologicalSexValue(HasLinkToValue):
    """
    Relating a human to a reification statement of the relation between the human and a biological sex of that human.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "hasBiologicalSexValue"
