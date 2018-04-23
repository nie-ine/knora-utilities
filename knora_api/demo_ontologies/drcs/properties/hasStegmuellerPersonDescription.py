#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...human.properties.hasDescription import HasDescription

"""
definition of property drcs:HasStegmuellerPersonDescription

created at: 2018-04-19 14:07:12
created from: drcs-ontology-knora.ttl
"""


class HasStegmuellerPersonDescription(HasDescription):
    """
    Relating a person to a Stegmüller's description (as object) thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/drcs"
        self._name = "hasStegmuellerPersonDescription"
