#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property information-carrier:HasSenderValue

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class HasSenderValue(HasLinkToValue):
    """
    Relating something to a reification statement of the relation between that something and a person who sent it.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/information-carrier"
        self._name = "hasSenderValue"
