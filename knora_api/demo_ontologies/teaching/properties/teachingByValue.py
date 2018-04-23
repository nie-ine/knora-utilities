#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...agent.properties.hasAgentValue import HasAgentValue

"""
definition of property teaching:TeachingByValue

created at: 2018-04-19 14:07:12
created from: teaching-ontology-knora.ttl
"""


class TeachingByValue(HasAgentValue):
    """
    Relating a teaching to a reification statement of the relation between the teaching and a person having the teacher role.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/teaching"
        self._name = "teachingByValue"
