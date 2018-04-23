#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text_editing.properties.hasEdition import HasEdition as Tex_HasEdition

"""
definition of property kuno-raeber:HasEdition

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class HasEdition(Tex_HasEdition):
    """
    Relating a text by Kuno Raeber to an edition thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "hasEdition"
