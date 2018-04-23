#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property language:ExpressedInDialectValue

created at: 2018-04-19 14:07:12
created from: language-ontology-knora.ttl
"""


class ExpressedInDialectValue(HasLinkToValue):
    """
    Relating a human expression to a reification statement of the relation between the expression and a dialect it is expressed in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/language"
        self._name = "expressedInDialectValue"
