#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property event:HasStateValue

created at: 2018-04-19 14:07:12
created from: event-ontology-knora.ttl
"""


class HasStateValue(HasLinkToValue):
    """
    Relating a resource to a reification statement of the relation between the resource and a state.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/event"
        self._name = "hasStateValue"
