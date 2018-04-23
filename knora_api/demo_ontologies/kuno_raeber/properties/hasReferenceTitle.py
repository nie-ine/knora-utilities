#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasTitle import HasTitle

"""
definition of property kuno-raeber:HasReferenceTitle

created at: 2018-04-19 14:07:12
created from: kuno-raeber-ontology-knora.ttl
"""


class HasReferenceTitle(HasTitle):
    """
    Relating a poem to a title (as object) of a reference poem.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/kuno-raeber"
        self._name = "hasReferenceTitle"
