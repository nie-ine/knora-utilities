#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasDescription import HasDescription as Tex_HasDescription

"""
definition of property publishing:HasDescription

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class HasDescription(Tex_HasDescription):
    """
    Relating a publication to a description thereof.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "hasDescription"
