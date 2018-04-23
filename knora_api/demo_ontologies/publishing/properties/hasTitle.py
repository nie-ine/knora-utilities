#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasTitle import HasTitle as Tex_HasTitle

"""
definition of property publishing:HasTitle

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class HasTitle(Tex_HasTitle):
    """
    Relating a publication to its title (as object).
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/publishing"
        self._name = "hasTitle"
