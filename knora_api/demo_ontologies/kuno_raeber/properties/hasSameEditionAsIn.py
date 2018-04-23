#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property kuno-raeber:HasSameEditionAsIn

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class HasSameEditionAsIn(HasLinkTo):
    """
    Relating a poem by Kuno Raeber to a convolute containing a poem with the same edition.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "hasSameEditionAsIn"
