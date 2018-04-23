#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasText import HasText

"""
definition of property drcs:HasStegmuellerCode

created at: 2018-04-19 14:07:12
created from: drcs-ontology-knora.ttl
"""


class HasStegmuellerCode(HasText):
    """
    Relating a commentary on Petrus Lombardus' Sentences to a Stegmüller's code (as object) thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/drcs"
        self._name = "hasStegmuellerCode"
