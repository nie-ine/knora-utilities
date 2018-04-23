#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...agent.properties.hasRoleValue import HasRoleValue as Age_HasRoleValue

"""
definition of property organisation:HasRoleValue

created at: 2018-04-19 14:07:12
created from: organisation-ontology-knora.ttl
"""


class HasRoleValue(Age_HasRoleValue):
    """
    Relating person organisation to a reification statement of the relation between the organisation and a role it has.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/organisation"
        self._name = "hasRoleValue"
