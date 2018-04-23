#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasDescription import HasDescription

"""
definition of property image:HasPhotographSourceDescription

created at: 2018-04-19 14:07:12
created from: image-ontology-knora.ttl
"""


class HasPhotographSourceDescription(HasDescription):
    """
    Relating something to a description (as object) of a source of a photograph of that something.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/image"
        self._name = "hasPhotographSourceDescription"
