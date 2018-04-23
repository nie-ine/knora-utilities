#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...event.properties.hasStateValue import HasStateValue

"""
definition of property publishing:HasPublishingStateValue

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class HasPublishingStateValue(HasStateValue):
    """
    Relating an expression to a reification statement of the relation between the expression and a publishing state thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "hasPublishingStateValue"
