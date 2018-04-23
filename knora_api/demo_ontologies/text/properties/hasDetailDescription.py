#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasDescription import HasDescription

"""
definition of property text:HasDetailDescription

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class HasDetailDescription(HasDescription):
    """
    Relating a resource to a description (as object) of its detail(s). E.g. in the case of a text a detail can be a passage variant or an emendation
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text"
        self._name = "hasDetailDescription"
