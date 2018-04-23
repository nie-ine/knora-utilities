#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasContent import HasContent

"""
definition of property text-editing:HasDiacriticalSign

created at: 2018-04-19 14:07:12
created from: text-editing-ontology-knora.ttl
"""


class HasDiacriticalSign(HasContent):
    """
    Relating a derived text expression to a sign (as object) indicating a textual aspect of the original text.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-editing"
        self._name = "hasDiacriticalSign"
