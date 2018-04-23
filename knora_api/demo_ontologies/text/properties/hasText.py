#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.textValue import TextValue

"""
definition of property text:HasText

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class HasText(TextValue):
    """
    Relating a resource to a text (as object) as a writable coherent set of signs representing semantics in a language.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text"
        self._name = "hasText"
