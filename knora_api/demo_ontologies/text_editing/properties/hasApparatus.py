#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...concept.properties.hasPartOf import HasPartOf

"""
definition of property text-editing:HasApparatus

created at: 2018-04-19 14:07:12
created from: text-editing-ontology-knora.ttl
"""


class HasApparatus(HasPartOf):
    """
    Relating a critical edition to its apparatus.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-editing"
        self._name = "hasApparatus"
