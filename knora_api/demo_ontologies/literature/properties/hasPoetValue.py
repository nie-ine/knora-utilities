#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasAuthorValue import HasAuthorValue

"""
definition of property literature:HasPoetValue

created at: 2018-04-19 14:07:12
created from: literature-ontology-knora.ttl
"""


class HasPoetValue(HasAuthorValue):
    """
    Relating a poem to a reification statement of the relation between the poem and a person who authored it.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/literature"
        self._name = "hasPoetValue"
