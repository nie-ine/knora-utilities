#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property physical-resource:HasLengthValue

created at: 2018-04-19 14:07:12
created from: physical-resource-ontology-knora.ttl
"""


class HasLengthValue(HasLinkToValue):
    """
    Relating a space to a reification statement of the relation between that space and its length.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/physical-resource"
        self._name = "hasLengthValue"
