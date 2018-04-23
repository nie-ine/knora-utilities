#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property text-structure:HasStructureValue

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class HasStructureValue(HasLinkToValue):
    """
    Relating a text expression to a reification statement of the relation between the text expression and its structure.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-structure"
        self._name = "hasStructureValue"
