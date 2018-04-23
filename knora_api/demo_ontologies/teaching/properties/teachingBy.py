#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...agent.properties.hasAgent import HasAgent

"""
definition of property teaching:TeachingBy

created at: 2018-04-19 14:07:12
created from: teaching-ontology-knora.ttl
"""


class TeachingBy(HasAgent):
    """
    Relating a teaching to a person having the teacher role.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/teaching"
        self._name = "teachingBy"
