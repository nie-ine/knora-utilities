#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property event:HasEvent

created at: 2018-04-19 14:07:12
created from: event-ontology-knora.ttl
"""


class HasEvent(HasLinkTo):
    """
    Relating someone or something - eg. an organisation, event, procedure - to an event.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/event"
        self._name = "hasEvent"
