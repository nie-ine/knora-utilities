#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property agent:HasAgent

created at: 2018-04-19 14:07:12
created from: agent-ontology-knora.ttl
"""


class HasAgent(HasLinkTo):
    """
    Relating an action to an agent acting in it.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/agent"
        self._name = "hasAgent"
