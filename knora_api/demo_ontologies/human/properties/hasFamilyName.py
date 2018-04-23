#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasName import HasName

"""
definition of property human:HasFamilyName

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class HasFamilyName(HasName):
    """
    Relating a person to a family name (as object) of that person.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "hasFamilyName"
