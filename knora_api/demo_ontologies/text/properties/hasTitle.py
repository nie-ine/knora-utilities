#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasText import HasText

"""
definition of property text:HasTitle

created at: 2018-04-19 14:07:12
created from: text-ontology-knora.ttl
"""


class HasTitle(HasText):
    """
    Relating a resource to a title (as object) as a textual identifier of the resource.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/text"
        self._name = "hasTitle"
