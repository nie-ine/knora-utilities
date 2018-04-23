#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasName import HasName
from ...text.properties.hasPreferredName import HasPreferredName as Tex_HasPreferredName

"""
definition of property human:HasPreferredName

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class HasPreferredName(HasName,Tex_HasPreferredName):
    """
    Relating a person to a preferred name (as object) of that person.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "hasPreferredName"
