#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property agent:HasRoleValue

created at: 2018-04-19 14:07:12
created from: agent-ontology-knora.ttl
"""


class HasRoleValue(HasLinkToValue):
    """
    Relating an agent to a reification statement of the relation between the agent and a role it,s/he has.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/agent"
        self._name = "hasRoleValue"
