#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkTo import HasLinkTo

"""
definition of property scholasticism:HasCommentaryMethod

created at: 2018-04-19 14:07:12
created from: scholasticism-ontology-knora.ttl
"""


class HasCommentaryMethod(HasLinkTo):
    """
    Relating a scholastic commentary to a method it adheres to.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/scholasticism"
        self._name = "hasCommentaryMethod"
