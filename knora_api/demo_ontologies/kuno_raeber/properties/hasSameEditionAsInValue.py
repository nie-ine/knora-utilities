#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property kuno-raeber:HasSameEditionAsInValue

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class HasSameEditionAsInValue(HasLinkToValue):
    """
    Relating a poem by Kuno Raeber to a reification statement of the relation between the poem and a convolute containing a poem with the same edition.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "hasSameEditionAsInValue"
