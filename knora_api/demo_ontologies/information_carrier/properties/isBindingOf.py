#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...physical_resource.properties.isPartOf import IsPartOf

"""
definition of property information-carrier:IsBindingOf

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class IsBindingOf(IsPartOf):
    """
    Relating a binding to a book it is part of.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/information-carrier"
        self._name = "isBindingOf"
