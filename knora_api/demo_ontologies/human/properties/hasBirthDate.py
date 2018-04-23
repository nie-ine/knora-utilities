#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.dateValue import DateValue

"""
definition of property human:HasBirthDate

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class HasBirthDate(DateValue):
    """
    Relating a person to a date of birth (as object) of that person.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "hasBirthDate"
