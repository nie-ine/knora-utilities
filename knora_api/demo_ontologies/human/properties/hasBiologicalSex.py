#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property human:HasBiologicalSex

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class HasBiologicalSex(HasLinkTo):
    """
    Relating a human to a biological sex of that human.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "hasBiologicalSex"
