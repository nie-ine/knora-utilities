#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...event.properties.isOutputOf import IsOutputOf

"""
definition of property human:HasCreating

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class HasCreating(IsOutputOf):
    """
    Relating a creation by a person to the creating thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "hasCreating"
