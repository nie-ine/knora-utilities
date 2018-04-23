#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property text-structure:StructureHasUnitValue

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class StructureHasUnitValue(HasLinkToValue):
    """
    Relating a text structure to a reification statement of the relation between the text structure and its unit.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-structure"
        self._name = "structureHasUnitValue"
