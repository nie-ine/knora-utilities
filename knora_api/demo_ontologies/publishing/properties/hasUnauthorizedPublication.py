#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasPublication import HasPublication

"""
definition of property publishing:HasUnauthorizedPublication

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class HasUnauthorizedPublication(HasPublication):
    """
    Relating an expression to a publication thereof without the author's authorization.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "hasUnauthorizedPublication"
