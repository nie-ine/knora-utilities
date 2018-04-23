#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property concept:IsPartOf

created at: 2018-04-19 14:07:12
created from: concept-ontology-knora.ttl
"""


class IsPartOf(HasLinkTo):
    """
    Relating a symbolic concept to another one it is part of.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/concept"
        self._name = "isPartOf"
