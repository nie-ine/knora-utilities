#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasDescription import HasDescription

"""
definition of property information-carrier:HasCarrierCollectionDescription

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class HasCarrierCollectionDescription(HasDescription):
    """
    Relating a convolute to a description (as object) of an information carrier collection it contains.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/information-carrier"
        self._name = "hasCarrierCollectionDescription"
