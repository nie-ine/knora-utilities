#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.dateValue import DateValue

"""
definition of property publishing:HasDate

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class HasDate(DateValue):
    """
    Relating a publication to the date it was published on.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "hasDate"
