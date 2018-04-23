#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...physical_resource.properties.isPartOf import IsPartOf

"""
definition of property agent:IsMemberOf

created at: 2018-04-19 14:07:12
created from: agent-ontology-knora.ttl
"""


class IsMemberOf(IsPartOf):
    """
    Relating an agent to a group the agent is a member of.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/agent"
        self._name = "isMemberOf"
