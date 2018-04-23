#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasDescription import HasDescription

"""
definition of property publishing:HasNachlassPublicationDescription

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class HasNachlassPublicationDescription(HasDescription):
    """
    Relating an expression to a description (as object) of its nachlass publication.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "hasNachlassPublicationDescription"
