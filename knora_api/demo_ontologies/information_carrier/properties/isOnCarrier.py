#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property information-carrier:IsOnCarrier

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class IsOnCarrier(HasLinkTo):
    """
    Relating an expression to an information carrier it is on.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/information-carrier"
        self._name = "isOnCarrier"
