#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property event:IsInputOfValue

created at: 2018-04-19 14:07:12
created from: event-ontology-knora.ttl
"""


class IsInputOfValue(HasLinkToValue):
    """
    Relating an input to a reification statement of the relation between the input and a process.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/event"
        self._name = "isInputOfValue"
