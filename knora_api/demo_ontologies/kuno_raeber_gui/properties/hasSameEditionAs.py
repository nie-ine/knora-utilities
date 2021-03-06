#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.intValue import IntValue

"""
definition of property kuno-raeber-gui:HasSameEditionAs

created at: 2018-04-19 14:07:12
created from: kuno-raeber-gui-ontology-knora.ttl
"""


class HasSameEditionAs(IntValue):
    """
    Relating a poem by Kuno Raeber to having or not the same edition as another poem in another convolute.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber-gui"
        self._name = "hasSameEditionAs"
