#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .personHasRole import PersonHasRole

"""
definition of property human:HasOccupationalRole

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class HasOccupationalRole(PersonHasRole):
    """
    Relating a person to a current occupational role the person has.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "hasOccupationalRole"
