#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasText import HasText

"""
definition of property publishing:HasPublicationNumber

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class HasPublicationNumber(HasText):
    """
    Relating an expression to its number (as object) in a publication.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "hasPublicationNumber"
