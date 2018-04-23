#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property agent:ActsIn

created at: 2018-04-19 14:07:12
created from: agent-ontology-knora.ttl
"""


class ActsIn(HasLinkTo):
    """
    Relating an agent to an action the agent is acting in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/agent"
        self._name = "actsIn"
