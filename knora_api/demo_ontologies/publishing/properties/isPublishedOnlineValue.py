#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property publishing:IsPublishedOnlineValue

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class IsPublishedOnlineValue(HasLinkToValue):
    """
    Relating an expression to a reification statement of the relation between the expression and its online publication as Web page.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "isPublishedOnlineValue"
