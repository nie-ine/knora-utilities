#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...agent.properties.actsInValue import ActsInValue as Age_ActsInValue

"""
definition of property human:ActsInValue

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class ActsInValue(Age_ActsInValue):
    """
    Relating a human to a reification statement of the relation between the human and an action the human is in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "actsInValue"
