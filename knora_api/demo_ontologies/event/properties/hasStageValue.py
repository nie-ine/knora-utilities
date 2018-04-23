#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property event:HasStageValue

created at: 2018-04-19 14:07:12
created from: event-ontology-knora.ttl
"""


class HasStageValue(HasLinkToValue):
    """
    Relating a process to a reification statement of the relation between the process and a stage thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/event"
        self._name = "hasStageValue"
