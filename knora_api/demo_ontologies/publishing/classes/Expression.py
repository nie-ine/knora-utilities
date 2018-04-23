#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ...concept.classes.Expression import Expression as con_Expression
from ..properties.isPublishedIn import IsPublishedIn
from .. import ONTOLOGY_NS, PROJECT_ID

"""
definition of class publishing:Expression

created at: 2018-04-19 14:07:12
created from: publishing-ontology-knora.ttl
"""


class Expression(con_Expression):
    """
    See http://iflastandards.info/ns/fr/frbr/frbroo/F24_Publication_Expression.

    Labels: Publikation-Expression (de) / publication expression (en)
    """
    def __init__(self, isPublishedIn=None, **kwargs):
        """

        :param isPublishedIn:
        :param kwargs:
        """

        super().__init__(**kwargs)

        self._namespace = ONTOLOGY_NS
        self._project_id = PROJECT_ID
        self._name = "Expression"

        self.isPublishedIn = IsPublishedIn(isPublishedIn)
