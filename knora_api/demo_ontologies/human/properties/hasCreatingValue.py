#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...event.properties.isOutputOfValue import IsOutputOfValue

"""
definition of property human:HasCreatingValue

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class HasCreatingValue(IsOutputOfValue):
    """
    Relating a creation by a person to a reification statement of the relation between the creation and the creating thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "hasCreatingValue"
