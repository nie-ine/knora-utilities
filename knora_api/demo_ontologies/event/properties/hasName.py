#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasName import HasName as Tex_HasName

"""
definition of property event:HasName

created at: 2018-04-19 14:07:12
created from: event-ontology-knora.ttl
"""


class HasName(Tex_HasName):
    """
    Relating an event to its name.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/event"
        self._name = "hasName"
