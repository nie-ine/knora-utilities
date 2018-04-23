#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property publishing:HasPublisherValue

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class HasPublisherValue(HasLinkToValue):
    """
    Relating a publication to a reification statement of the relation between the publication and its publisher.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "hasPublisherValue"
