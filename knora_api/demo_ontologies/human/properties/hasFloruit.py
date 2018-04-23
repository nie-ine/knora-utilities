#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .actsIn import ActsIn

"""
definition of property human:HasFloruit

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class HasFloruit(ActsIn):
    """
    Relating a person to a floruit the person has.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "hasFloruit"
