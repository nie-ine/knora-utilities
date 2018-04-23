#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...agent.properties.hasRole import HasRole as Age_HasRole

"""
definition of property organisation:HasRole

created at: 2018-04-19 14:07:12
created from: organisation-ontology-knora.ttl
"""


class HasRole(Age_HasRole):
    """
    Relating a person organisation to a role it has.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/organisation"
        self._name = "hasRole"
