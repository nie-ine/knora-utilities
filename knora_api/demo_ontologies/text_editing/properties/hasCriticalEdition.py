#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasEdition import HasEdition

"""
definition of property text-editing:HasCriticalEdition

created at: 2018-04-19 14:07:12
created from: text-editing-ontology-knora.ttl
"""


class HasCriticalEdition(HasEdition):
    """
    Relating a text expression to a critical edition thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-editing"
        self._name = "hasCriticalEdition"
