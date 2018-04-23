#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property agent:HasAgentValue

created at: 2018-04-19 14:07:12
created from: agent-ontology-knora.ttl
"""


class HasAgentValue(HasLinkToValue):
    """
    Relating an action to a reification statement of the relation between the action and an agent acting in it.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/agent"
        self._name = "hasAgentValue"
