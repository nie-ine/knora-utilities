#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasDescription import HasDescription

"""
definition of property information-carrier:ConvoluteHasContentRepresentation

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class ConvoluteHasContentRepresentation(HasDescription):
    """
    Relating a convolute to a description (as object) of its content representation.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/information-carrier"
        self._name = "convoluteHasContentRepresentation"
