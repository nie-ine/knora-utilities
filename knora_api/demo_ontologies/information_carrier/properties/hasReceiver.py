#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property information-carrier:HasReceiver

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class HasReceiver(HasLinkTo):
    """
    Relating something to a person who received it.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/information-carrier"
        self._name = "hasReceiver"
