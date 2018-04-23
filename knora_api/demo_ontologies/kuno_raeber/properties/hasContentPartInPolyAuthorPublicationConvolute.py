#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property kuno-raeber:HasContentPartInPolyAuthorPublicationConvolute

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class HasContentPartInPolyAuthorPublicationConvolute(HasLinkTo):
    """
    Relating a poly-author publication to a convolute it has part of its content in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "hasContentPartInPolyAuthorPublicationConvolute"
