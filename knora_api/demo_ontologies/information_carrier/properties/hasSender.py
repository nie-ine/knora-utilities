#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property information-carrier:HasSender

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class HasSender(HasLinkTo):
    """
    Relating something to a person who sent it.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/information-carrier"
        self._name = "hasSender"
