#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.properties.isInManuscriptValue import IsInManuscriptValue

"""
definition of property kuno-raeber:IsInNotebookValue

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class IsInNotebookValue(IsInManuscriptValue):
    """
    Relating a poem note by Kuno Raeber to a reification statement of the relation between the poem note and a notebook it is in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "isInNotebookValue"
