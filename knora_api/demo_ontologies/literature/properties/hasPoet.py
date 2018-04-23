#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasAuthor import HasAuthor

"""
definition of property literature:HasPoet

created at: 2018-04-19 14:07:12
created from: literature-ontology-knora.ttl
"""


class HasPoet(HasAuthor):
    """
    Relating a poem to a person who authored it.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/literature"
        self._name = "hasPoet"
