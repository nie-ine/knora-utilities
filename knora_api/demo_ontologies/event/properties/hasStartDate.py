#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.dateValue import DateValue

"""
definition of property event:HasStartDate

created at: 2018-04-19 14:07:12
created from: event-ontology-knora.ttl
"""


class HasStartDate(DateValue):
    """
    Relating an event to its start date.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/event"
        self._name = "hasStartDate"
