#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property text:HasReferenceTextValue

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class HasReferenceTextValue(HasLinkToValue):
    """
    Relating a text to a reification statement of the relation between the text and another one as its reference.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text"
        self._name = "hasReferenceTextValue"
