#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasReferenceTextValue import HasReferenceTextValue

"""
definition of property kuno-raeber:HasReferencePoemValue

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class HasReferencePoemValue(HasReferenceTextValue):
    """
    Relating a poem to a reification statement of the relation between the poem and another one as its reference.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "hasReferencePoemValue"
