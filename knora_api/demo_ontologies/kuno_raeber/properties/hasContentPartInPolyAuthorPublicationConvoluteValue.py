#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property kuno-raeber:HasContentPartInPolyAuthorPublicationConvoluteValue

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class HasContentPartInPolyAuthorPublicationConvoluteValue(HasLinkToValue):
    """
    Relating a poly-author publication to a reification statement of the relation between the publication and a convolute it has part of its content in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "hasContentPartInPolyAuthorPublicationConvoluteValue"
