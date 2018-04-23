#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property publishing:IsPublishedOnline

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class IsPublishedOnline(HasLinkTo):
    """
    Relating an expression to its online publication as Web page.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "isPublishedOnline"
