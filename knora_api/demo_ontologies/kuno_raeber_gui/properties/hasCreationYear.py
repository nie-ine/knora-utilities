#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.dateValue import DateValue

"""
definition of property kuno-raeber-gui:HasCreationYear

created at: 2018-04-19 14:07:12
created from: kuno-raeber-gui-ontology-knora.ttl
"""


class HasCreationYear(DateValue):
    """
    Relating a poem by Kuno Raeber to a creation year.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber-gui"
        self._name = "hasCreationYear"
