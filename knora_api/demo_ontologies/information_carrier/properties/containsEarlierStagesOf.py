#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property information-carrier:ContainsEarlierStagesOf

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class ContainsEarlierStagesOf(HasLinkTo):
    """
    Relating a convolute to another one whose information carriers bear later stages of the texts on the carriers of the former.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/information-carrier"
        self._name = "containsEarlierStagesOf"
