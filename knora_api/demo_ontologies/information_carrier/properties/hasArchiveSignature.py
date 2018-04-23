#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasIdentifier import HasIdentifier

"""
definition of property information-carrier:HasArchiveSignature

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class HasArchiveSignature(HasIdentifier):
    """
    Relating an element of an archive to its signature (as object) as identifier.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/information-carrier"
        self._name = "hasArchiveSignature"
