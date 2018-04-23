#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .personHasRoleValue import PersonHasRoleValue

"""
definition of property human:HasOccupationalRoleValue

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class HasOccupationalRoleValue(PersonHasRoleValue):
    """
    Relating a person to a reification statement of the relation between the person and a current occupational role the person has.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "hasOccupationalRoleValue"
