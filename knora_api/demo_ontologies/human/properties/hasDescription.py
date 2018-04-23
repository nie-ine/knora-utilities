#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasDescription import HasDescription as Tex_HasDescription

"""
definition of property human:HasDescription

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class HasDescription(Tex_HasDescription):
    """
    Relating a person to a description (as object) of that person.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "hasDescription"
