#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property text:HasCopyist

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class HasCopyist(HasLinkTo):
    """
    Relating a text to a person who copied it by handwriting.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text"
        self._name = "hasCopyist"
