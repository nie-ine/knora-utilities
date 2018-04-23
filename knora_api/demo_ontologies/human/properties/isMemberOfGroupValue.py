#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...agent.properties.isMemberOfValue import IsMemberOfValue

"""
definition of property human:IsMemberOfGroupValue

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class IsMemberOfGroupValue(IsMemberOfValue):
    """
    Relating a person to a reification statement of the relation between the person and a group the person is a member of.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "isMemberOfGroupValue"
