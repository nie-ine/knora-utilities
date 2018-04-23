#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property event:HasState

created at: 2018-04-19 14:07:12
created from: event-ontology-knora.ttl
"""


class HasState(HasLinkTo):
    """
    Relating a resource to a state.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/event"
        self._name = "hasState"
