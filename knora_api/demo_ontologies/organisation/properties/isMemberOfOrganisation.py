#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.properties.isMemberOfGroup import IsMemberOfGroup

"""
definition of property organisation:IsMemberOfOrganisation

created at: 2018-04-19 14:07:12
created from: organisation-ontology-knora.ttl
"""


class IsMemberOfOrganisation(IsMemberOfGroup):
    """
    Relating a person to an organisation the person is a member of.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/organisation"
        self._name = "isMemberOfOrganisation"
