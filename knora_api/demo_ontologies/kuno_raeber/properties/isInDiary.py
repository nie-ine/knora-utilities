#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...information_carrier.properties.isInDiary import IsInDiary as Inf_IsInDiary

"""
definition of property kuno-raeber:IsInDiary

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class IsInDiary(Inf_IsInDiary):
    """
    Relating a diary entry by Kuno Raeber to the diary it is in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "isInDiary"
