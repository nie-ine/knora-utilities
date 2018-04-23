#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasPublicationValue import HasPublicationValue

"""
definition of property publishing:HasUnauthorizedPublicationValue

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class HasUnauthorizedPublicationValue(HasPublicationValue):
    """
    Relating an expression to a reification statement of the relation between the expression and a publication thereof without the author's authorization.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "hasUnauthorizedPublicationValue"
