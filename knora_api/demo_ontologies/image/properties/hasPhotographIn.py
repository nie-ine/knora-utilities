#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property image:HasPhotographIn

created at: 2018-04-19 14:07:12
created from: image-ontology-knora.ttl
"""


class HasPhotographIn(HasLinkTo):
    """
    Relating something to something else containing a photograph of the former.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/image"
        self._name = "hasPhotographIn"
