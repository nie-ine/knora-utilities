#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasName import HasName as Tex_HasName

"""
definition of property human:HasName

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class HasName(Tex_HasName):
    """
    Relating a person to a name (as object) of that person.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "hasName"
