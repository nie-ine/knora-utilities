#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property agent:HasRole

created at: 2018-04-19 14:07:12
created from: agent-ontology-knora.ttl
"""


class HasRole(HasLinkTo):
    """
    Relating an agent to a role it,s/he has.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/agent"
        self._name = "hasRole"
