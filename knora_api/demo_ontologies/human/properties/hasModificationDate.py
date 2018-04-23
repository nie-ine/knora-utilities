#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.dateValue import DateValue

"""
definition of property human:HasModificationDate

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class HasModificationDate(DateValue):
    """
    Relating a human creation to its modification date.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "hasModificationDate"
