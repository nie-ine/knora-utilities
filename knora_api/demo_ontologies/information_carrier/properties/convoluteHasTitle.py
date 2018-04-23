#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasTitle import HasTitle

"""
definition of property information-carrier:ConvoluteHasTitle

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class ConvoluteHasTitle(HasTitle):
    """
    Relating a convolute to its titel (as object).
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/information-carrier"
        self._name = "convoluteHasTitle"
