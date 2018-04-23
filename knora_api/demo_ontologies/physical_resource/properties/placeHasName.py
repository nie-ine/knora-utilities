#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasName import HasName

"""
definition of property physical-resource:PlaceHasName

created at: 2018-04-19 14:07:12
created from: physical-resource-ontology-knora.ttl
"""


class PlaceHasName(HasName):
    """
    Relating a place to its name.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/physical-resource"
        self._name = "placeHasName"
