#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property human:AdheringToThought

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class AdheringToThought(HasLinkTo):
    """
    Relating a person to a body of thought the person adheres to.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "adheringToThought"
