#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.textValue import TextValue

"""
definition of property kuno-raeber-gui:HasPoemText

created at: 2018-04-19 14:07:12
created from: kuno-raeber-gui-ontology-knora.ttl
"""


class HasPoemText(TextValue):
    """
    Relating a poem by Kuno Raeber to its text content.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber-gui"
        self._name = "hasPoemText"
