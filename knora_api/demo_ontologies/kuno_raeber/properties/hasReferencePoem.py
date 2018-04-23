#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasReferenceText import HasReferenceText

"""
definition of property kuno-raeber:HasReferencePoem

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class HasReferencePoem(HasReferenceText):
    """
    Relating a poem to another one as its reference.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "hasReferencePoem"
