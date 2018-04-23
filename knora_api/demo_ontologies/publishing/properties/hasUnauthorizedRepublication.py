#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasPublication import HasPublication

"""
definition of property publishing:HasUnauthorizedRepublication

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class HasUnauthorizedRepublication(HasPublication):
    """
    Relating an expression to a republication thereof without the author's authorization.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "hasUnauthorizedRepublication"
