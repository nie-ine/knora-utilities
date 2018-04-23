#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasDescription import HasDescription

"""
definition of property publishing:HasPublisherDescription

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class HasPublisherDescription(HasDescription):
    """
    Relating a publication to its publisher's description (as object).
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "hasPublisherDescription"
