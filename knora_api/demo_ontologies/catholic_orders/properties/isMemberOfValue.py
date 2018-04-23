#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.properties.isMemberOfOrganisationValue import IsMemberOfOrganisationValue

"""
definition of property catholic-orders:IsMemberOfValue

created at: 2018-04-19 14:07:12
created from: catholic-orders-ontology-knora.ttl
"""


class IsMemberOfValue(IsMemberOfOrganisationValue):
    """
    Relating a person to a reification statement of the relation between the person and a catholic order the person is a member of.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/catholic-orders"
        self._name = "isMemberOfValue"
