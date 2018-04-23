#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.properties.hasRoleValue import HasRoleValue as Hum_HasRoleValue

"""
definition of property scholasticism:HasRoleValue

created at: 2018-04-19 14:07:12
created from: scholasticism-ontology-knora.ttl
"""


class HasRoleValue(Hum_HasRoleValue):
    """
    Relating a scholastic to a statement as reification of the relation between the scholastic and a role he has.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/scholasticism"
        self._name = "hasRoleValue"
