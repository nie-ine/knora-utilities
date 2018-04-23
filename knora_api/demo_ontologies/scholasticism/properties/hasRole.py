#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.properties.hasRole import HasRole as Hum_HasRole

"""
definition of property scholasticism:HasRole

created at: 2018-04-19 14:07:12
created from: scholasticism-ontology-knora.ttl
"""


class HasRole(Hum_HasRole):
    """
    Relating a scholastic to a role he has.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/scholasticism"
        self._name = "hasRole"
