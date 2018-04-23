#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasAlias import HasAlias as Tex_HasAlias

"""
definition of property human:HasAlias

created at: 2018-04-19 14:07:12
created from: human-ontology-knora.ttl
"""


class HasAlias(Tex_HasAlias):
    """
    Relating a person to an alias (as object) of that person.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/human"
        self._name = "hasAlias"
