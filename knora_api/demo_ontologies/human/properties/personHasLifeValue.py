#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...event.properties.hasExistenceValue import HasExistenceValue

"""
definition of property human:PersonHasLifeValue

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class PersonHasLifeValue(HasExistenceValue):
    """
    Relating a person to a reification statement of the relation between the person and the person's life.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "personHasLifeValue"
