#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasEditionValue import HasEditionValue

"""
definition of property text-editing:HasCriticalEditionValue

created at: 2018-04-19 14:07:12
created from: text-editing-ontology-knora.ttl
"""


class HasCriticalEditionValue(HasEditionValue):
    """
    Relating a text expression to a reification statement of the relation between the text and a critical edition thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-editing"
        self._name = "hasCriticalEditionValue"
