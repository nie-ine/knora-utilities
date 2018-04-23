#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...event.properties.hasExistence import HasExistence

"""
definition of property human:PersonHasLife

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class PersonHasLife(HasExistence):
    """
    Relating a person to the person's life.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "personHasLife"
