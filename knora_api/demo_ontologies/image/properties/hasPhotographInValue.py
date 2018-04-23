#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property image:HasPhotographInValue

created at: 2018-04-19 14:07:12
created from: image-ontology-knora.ttl
"""


class HasPhotographInValue(HasLinkToValue):
    """
    Relating something to a reification statement of the relation between that something and something else containing a photograph of the former.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/image"
        self._name = "hasPhotographInValue"
