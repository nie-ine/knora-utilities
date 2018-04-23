#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property text-editing:HasSameEditionAs

created at: 2018-04-19 14:07:12
created from: text-editing-ontology-knora.ttl
"""


class HasSameEditionAs(HasLinkTo):
    """
    Relating two texts with a same edition.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text-editing"
        self._name = "hasSameEditionAs"
