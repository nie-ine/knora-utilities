#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .containsEarlierStagesOf import ContainsEarlierStagesOf

"""
definition of property information-carrier:ContainsEarlierStagesOfPublication

created at: 2018-04-19 14:07:12
created from: information-carrier-ontology-knora.ttl
"""


class ContainsEarlierStagesOfPublication(ContainsEarlierStagesOf):
    """
    Relating a convolute to another one whose information carriers bear later publication stages of the texts on the carriers of the former.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/information-carrier"
        self._name = "containsEarlierStagesOfPublication"
