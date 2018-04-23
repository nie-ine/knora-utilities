#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.dateValue import DateValue

"""
definition of property human:HasCreationDate

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class HasCreationDate(DateValue):
    """
    Relating a creation by a person to a date it was created on.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "hasCreationDate"
