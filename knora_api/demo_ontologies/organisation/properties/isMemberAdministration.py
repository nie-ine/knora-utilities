#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .isMemberOfOrganisation import IsMemberOfOrganisation

"""
definition of property organisation:IsMemberAdministration

created at: 2018-04-19 14:07:12
created from: organisation-ontology-knora.ttl
"""


class IsMemberAdministration(IsMemberOfOrganisation):
    """
    Relating a person to an administration the person is a member of.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/organisation"
        self._name = "isMemberAdministration"
