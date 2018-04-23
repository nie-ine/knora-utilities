#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.properties.hasCreationDate import HasCreationDate

"""
definition of property information-carrier:HasDiaryEnteringDate

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class HasDiaryEnteringDate(HasCreationDate):
    """
    Relating a diary entry to its date of entering in a diary.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/information-carrier"
        self._name = "hasDiaryEnteringDate"
