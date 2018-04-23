#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.booleanValue import BooleanValue

"""
definition of property kuno-raeber:HasStrophe

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class HasStrophe(BooleanValue):
    """
    Relating a poem by Kuno Raeber to having a strophe or not.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "hasStrophe"
