#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasComment import HasComment

"""
definition of property language:HasLinguisticComment

created at: 2018-04-19 14:07:12
created from: language-ontology-knora.ttl
"""


class HasLinguisticComment(HasComment):
    """
    Relating a human natural language expression to a linguistic comment (as object) as a textual statement about the resource.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/language"
        self._name = "hasLinguisticComment"
