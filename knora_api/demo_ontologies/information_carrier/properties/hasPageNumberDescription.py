#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.textValue import TextValue

"""
definition of property information-carrier:HasPageNumberDescription

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class HasPageNumberDescription(TextValue):
    """
    Relating an expression to a description (as object) of the number(s) of and possibly a location on (a) pages it is on; examples of the string of its value: "001-002", "01 recto", "O2 (bottom)".
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/information-carrier"
        self._name = "hasPageNumberDescription"
