#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .isMemberOfOrganisationValue import IsMemberOfOrganisationValue

"""
definition of property organisation:IsMemberOfAdministrationValue

created at: 2018-04-19 14:07:12
created from: organisation-ontology-knora.ttl
"""


class IsMemberOfAdministrationValue(IsMemberOfOrganisationValue):
    """
    Relating a person to a reification statement of the relation between the person and an organisation the person is a member of.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/organisation"
        self._name = "isMemberOfAdministrationValue"
