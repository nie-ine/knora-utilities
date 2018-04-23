#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...agent.properties.isMemberOf import IsMemberOf

"""
definition of property human:IsMemberOfGroup

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class IsMemberOfGroup(IsMemberOf):
    """
    Relating a person to a group the person is a member of.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "isMemberOfGroup"
