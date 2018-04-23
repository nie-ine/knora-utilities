#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...agent.properties.actsIn import ActsIn as Age_ActsIn

"""
definition of property human:ActsIn

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class ActsIn(Age_ActsIn):
    """
    Relating a human to an action the human is in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "actsIn"
