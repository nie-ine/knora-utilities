#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasDescription import HasDescription

"""
definition of property event:HasGenesisDescription

created at: 2018-04-19 14:07:12
created from: event-ontology-knora.ttl
"""


class HasGenesisDescription(HasDescription):
    """
    Relating something to a description (as object) of the genesis thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/event"
        self._name = "hasGenesisDescription"
