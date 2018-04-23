#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasDescription import HasDescription

"""
definition of property text:HasSpecialDescription

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class HasSpecialDescription(HasDescription):
    """
    Relating a resource to a description (as object) of (a) certain feature(s).
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text"
        self._name = "hasSpecialDescription"
