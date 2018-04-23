#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasDiacriticalSign import HasDiacriticalSign

"""
definition of property text-editing:HasPageIndicator

created at: 2018-04-19 14:07:12
created from: text-editing-ontology-knora.ttl
"""


class HasPageIndicator(HasDiacriticalSign):
    """
    Relating a derived text expression to a diacritical sign (as object) that indicates where a page starts.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-editing"
        self._name = "hasPageIndicator"
