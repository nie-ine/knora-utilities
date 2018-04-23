#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property physical-resource:HasSize

created at: 2018-04-19 14:07:12
created from: physical-resource-ontology-knora.ttl
"""


class HasSize(HasLinkTo):
    """
    Relating a space to its size.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/physical-resource"
        self._name = "hasSize"
