#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...agent.properties.actsInValue import ActsInValue as Age_ActsInValue

"""
definition of property organisation:ActsInValue

created at: 2018-04-19 14:07:12
created from: organisation-ontology-knora.ttl
"""


class ActsInValue(Age_ActsInValue):
    """
    Relating person organisation to a reification statement of the relation between the organisation and an action it is acting in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/organisation"
        self._name = "actsInValue"
