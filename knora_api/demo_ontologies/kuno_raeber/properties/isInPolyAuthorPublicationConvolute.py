#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property kuno-raeber:IsInPolyAuthorPublicationConvolute

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class IsInPolyAuthorPublicationConvolute(HasLinkTo):
    """
    Relating a publication poem by Kuno Raeber to a poly-author publication it is in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "isInPolyAuthorPublicationConvolute"
