#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property human:AdheringToThoughtValue

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class AdheringToThoughtValue(HasLinkToValue):
    """
    Relating a person to a reification statement of the relation between the person and a body of thought the person adheres to.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "adheringToThoughtValue"
