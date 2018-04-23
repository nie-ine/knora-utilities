#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasPublication import HasPublication

"""
definition of property publishing:HasPolyAuthorPublication

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class HasPolyAuthorPublication(HasPublication):
    """
    Relating an expression to a publication thereof containing also expressions of other authors.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "hasPolyAuthorPublication"
