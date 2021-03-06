#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property text-structure:HasStrophe

created at: 2018-04-19 14:07:12
created from: text-structure-ontology-knora.ttl
"""


class HasStrophe(HasLinkTo):
    """
    Relating a verse poem to a strophe it contains.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-structure"
        self._name = "hasStrophe"
