#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...agent.properties.actsIn import ActsIn as Age_ActsIn

"""
definition of property organisation:ActsIn

created at: 2018-04-19 14:07:12
created from: organisation-ontology-knora.ttl
"""


class ActsIn(Age_ActsIn):
    """
    Relating a person organisation to an action it is acting in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/organisation"
        self._name = "actsIn"
