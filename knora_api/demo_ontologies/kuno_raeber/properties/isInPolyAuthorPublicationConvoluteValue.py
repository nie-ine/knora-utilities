#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property kuno-raeber:IsInPolyAuthorPublicationConvoluteValue

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class IsInPolyAuthorPublicationConvoluteValue(HasLinkToValue):
    """
    Relating a publication poem by Kuno Raeber to a reification statement of the relation between the poem and a poly-author publication it is in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "isInPolyAuthorPublicationConvoluteValue"
