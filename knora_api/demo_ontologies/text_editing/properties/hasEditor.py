#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property text-editing:HasEditor

created at: 2018-04-19 14:07:12
created from: text-editing-ontology-knora.ttl
"""


class HasEditor(HasLinkTo):
    """
    Relating a text to a person who edited it.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-editing"
        self._name = "hasEditor"
