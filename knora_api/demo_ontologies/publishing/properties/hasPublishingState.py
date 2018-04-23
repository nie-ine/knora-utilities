#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...event.properties.hasState import HasState

"""
definition of property publishing:HasPublishingState

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class HasPublishingState(HasState):
    """
    Relating an expression to a publishing state thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "hasPublishingState"
