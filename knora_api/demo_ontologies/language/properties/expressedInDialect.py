#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property language:ExpressedInDialect

created at: 2018-04-19 14:07:12
created from: language-ontology-knora.ttl
"""


class ExpressedInDialect(HasLinkTo):
    """
    Relating a human expression to a dialect it is expressed in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/language"
        self._name = "expressedInDialect"
