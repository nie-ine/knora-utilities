#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...knora_base.properties.hasLinkToValue import HasLinkToValue

"""
definition of property scholasticism:HasCommentaryFormValue

created at: 2018-04-19 14:07:12
created from: scholasticism-ontology-knora.ttl
"""


class HasCommentaryFormValue(HasLinkToValue):
    """
    Relating a scholastic commentary to a statement as reification of the relation between the scholastic commentary and a form it is represented in.
    """

    def __init__(self, argument):
        """

        :param argument:
        """
        super().__init__(argument)

        self._namespace = "http://www.knora.org/ontology/scholasticism"
        self._name = "hasCommentaryFormValue"
