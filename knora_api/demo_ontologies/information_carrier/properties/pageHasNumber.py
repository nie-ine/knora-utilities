#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.textValue import TextValue

"""
definition of property information-carrier:PageHasNumber

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class PageHasNumber(TextValue):
    """
    Relating a page to the number (as object) it has.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/information-carrier"
        self._name = "pageHasNumber"
