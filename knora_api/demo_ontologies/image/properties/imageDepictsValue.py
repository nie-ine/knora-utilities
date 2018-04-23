#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property image:ImageDepictsValue

created at: 2018-04-19 14:07:12
created from: image-ontology-knora.ttl
"""


class ImageDepictsValue(HasLinkToValue):
    """
    Relating an image to a reification statement of the relation between the image and what it depicts.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/image"
        self._name = "imageDepictsValue"
