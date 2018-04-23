#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...text.properties.hasComment import HasComment

"""
definition of property indology:HasIndologicComment

created at: 2018-04-19 14:07:12
created from: indology-ontology-knora.ttl
"""


class HasIndologicComment(HasComment):
    """
    Relating something to an Indological comment (as object) as a textual statement about that something.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/indology"
        self._name = "hasIndologicComment"
