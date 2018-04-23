#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...agent.properties.hasRole import HasRole

"""
definition of property human:PersonHasRole

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class PersonHasRole(HasRole):
    """
    Relating a person to a role the person has.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "personHasRole"
