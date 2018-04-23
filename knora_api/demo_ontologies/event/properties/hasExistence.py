#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasEvent import HasEvent

"""
definition of property event:HasExistence

created at: 2018-04-19 14:07:12
created from: event-ontology-knora.ttl
"""


class HasExistence(HasEvent):
    """
    Relating someone or something to her/his/its existence.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/event"
        self._name = "hasExistence"
