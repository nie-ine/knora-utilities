#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property publishing:HasPublisher

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class HasPublisher(HasLinkTo):
    """
    Relating a publication to its publisher.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "hasPublisher"
