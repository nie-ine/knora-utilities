#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasEventValue import HasEventValue

"""
definition of property event:HasExistenceValue

created at: 2018-04-19 14:07:12
created from: event-ontology-knora.ttl
"""


class HasExistenceValue(HasEventValue):
    """
    Relating someone or something to a reification statement of the relation between that someone or something and her/his/its existence.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/event"
        self._name = "hasExistenceValue"
