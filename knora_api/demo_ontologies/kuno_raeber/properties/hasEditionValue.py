#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text_editing.properties.hasEditionValue import HasEditionValue as Tex_HasEditionValue

"""
definition of property kuno-raeber:HasEditionValue

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class HasEditionValue(Tex_HasEditionValue):
    """
    Relating a text by Kuno Raeber to a reification statement of the relation between the text and an edition thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "hasEditionValue"
