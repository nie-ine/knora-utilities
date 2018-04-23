#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...concept.properties.hasPartValue import HasPartValue

"""
definition of property text-editing:HasApparatusValue

created at: 2018-04-19 14:07:12
created from: text-editing-ontology-knora.ttl
"""


class HasApparatusValue(HasPartValue):
    """
    Relating a critical edition to a reification statement of the relation between the edition and its apparatus.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-editing"
        self._name = "hasApparatusValue"
